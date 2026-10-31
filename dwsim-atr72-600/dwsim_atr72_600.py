"""
DWSim ATR 72-600 MCDU support for MobiFlight in X-Plane 12

Mirrors the ATR's MCDU screen to a WinWing (WinCTRL) MCDU.

The DWSim ATR 72-600 publishes its MCDU screens with the same encoding as X-Plane's default
FMS datarefs, under its own prefix:
- DWSim/ATR_Series/mcdu1/text_line0..15  (captain), mcdu2/... (first officer)
- each text line is a 96-byte ASCII buffer; the first 24 characters are the screen line,
  the rest is space padding
- each style line is 24 bytes, one per column: low 4 bits = colour (X-Plane FMS colour
  index), bit 7 = large font (data lines; labels are small), bit 6 = reverse video

Line layout (verified in the sim):
- lines 0-12: title + 6 label/data line pairs -> screen rows 0-12
- line 13:    spare line (messages)
- line 14:    scratchpad
- line 15:    unused
The WinWing screen has 14 rows, so its bottom row shows the scratchpad (line 14), or
line 13 when the scratchpad is empty.
"""

import asyncio
import base64
import json
import logging
import os
import urllib.request
from enum import StrEnum

import websockets

CDU_COLUMNS = 24
CDU_ROWS = 14
CDU_CELLS = CDU_COLUMNS * CDU_ROWS

ATR_LINES = 16
CONTENT_LINES = 13  # lines 0-12 map 1:1 to screen rows 0-12
SPARE_LINE = 13
SCRATCHPAD_LINE = 14

WEBSOCKET_HOST = "localhost"
WEBSOCKET_PORT = 8320

BASE_REST_URL = "http://localhost:8086/api/v2/datarefs"
BASE_WEBSOCKET_URI = f"ws://{WEBSOCKET_HOST}:8086/api/v2"

WS_CAPTAIN = f"ws://{WEBSOCKET_HOST}:{WEBSOCKET_PORT}/winwing/cdu-captain"
WS_CO_PILOT = f"ws://{WEBSOCKET_HOST}:{WEBSOCKET_PORT}/winwing/cdu-co-pilot"

DATAREF_PREFIX = "DWSim/ATR_Series"

# X-Plane FMS colour indexes -> WinWing colour codes
COLOR_MAP = {
    0: "e",  # Grey instead of black, which doesn't exist
    1: "c",
    2: "r",
    3: "y",
    4: "g",
    5: "m",
    6: "a",
    7: "w",
}

# The ATR's FMS is a Thales unit
FONT_REQUEST = json.dumps({"Target": "Font", "Data": "AirbusThales"})


class CduDevice(StrEnum):
    Captain = "mcdu1"
    CoPilot = "mcdu2"

    def get_endpoint(self) -> str:
        match self:
            case CduDevice.Captain:
                return WS_CAPTAIN
            case CduDevice.CoPilot:
                return WS_CO_PILOT
            case _:
                raise KeyError(f"Invalid device specified {self}")

    def get_dataref_prefix(self) -> str:
        return f"{DATAREF_PREFIX}/{self}/"

    def get_text_dataref(self, line) -> str:
        return f"{DATAREF_PREFIX}/{self}/text_line{line}"

    def get_style_dataref(self, line) -> str:
        return f"{DATAREF_PREFIX}/{self}/style_line{line}"


def fetch_dataref_mapping(device: CduDevice) -> dict[int, str]:
    """Returns {dataref id: dataref name} for this MCDU's text and style lines."""
    wanted = {device.get_text_dataref(line) for line in range(ATR_LINES)}
    wanted |= {device.get_style_dataref(line) for line in range(ATR_LINES)}

    with urllib.request.urlopen(BASE_REST_URL, timeout=5) as response:
        response_json = json.load(response)

    return {
        int(dataref["id"]): str(dataref["name"])
        for dataref in response_json["data"]
        if dataref["name"] in wanted
    }


def color_from_style(style):
    # Only colour indexes 0-7 are defined; default to white for anything else.
    return COLOR_MAP.get(style & 0xF, "w")


def size_from_style(style):
    # MobiFlight sizes: 0 = large, 1 = small
    return 0 if style & (1 << 7) else 1


def reverse_video_from_style(style):
    return 1 if style & (1 << 6) else 0


def line_text(device: CduDevice, values: dict[str, str | bytes], line: int) -> str | None:
    return values.get(device.get_text_dataref(line))


def render_line(device: CduDevice, values: dict[str, str | bytes], line: int, grid_row: int, display_data: list):
    """
    Renders one ATR MCDU line into a row of the WinWing 14-row grid.
    Rows are left blank until both the text and the style of the line have been received.
    """
    text = line_text(device, values, line)
    style = values.get(device.get_style_dataref(line))

    if text is None or style is None:
        return

    text = text[:CDU_COLUMNS].ljust(CDU_COLUMNS)

    for col in range(min(CDU_COLUMNS, len(style))):
        char = text[col]

        if char == " ":
            continue

        display_data[grid_row * CDU_COLUMNS + col] = [
            char,
            color_from_style(style[col]),
            size_from_style(style[col]),
            reverse_video_from_style(style[col]),
        ]


def generate_display_json(device: CduDevice, values: dict[str, str | bytes]) -> str:
    display_data = [[] for _ in range(CDU_CELLS)]

    for line in range(CONTENT_LINES):
        render_line(device, values, line, line, display_data)

    # Bottom row: scratchpad, or the spare (message) line when the scratchpad is empty.
    scratchpad = line_text(device, values, SCRATCHPAD_LINE) or ""
    bottom_line = SCRATCHPAD_LINE if scratchpad[:CDU_COLUMNS].strip() else SPARE_LINE
    render_line(device, values, bottom_line, CDU_ROWS - 1, display_data)

    return json.dumps({"Target": "Display", "Data": display_data})


async def handle_device_update(queue: asyncio.Queue, device: CduDevice):
    """
    Translates dataref updates and sends them to MobiFlight.
    """
    last_run_time = 0
    rate_limit_time = 0.1

    endpoint = device.get_endpoint()
    logging.info("Connecting to CDU device %s", device)
    async for websocket in websockets.connect(endpoint):
        logging.info("Connected successfully to CDU device %s", device)
        await websocket.send(FONT_REQUEST)
        while True:
            values = await queue.get()

            try:
                # Rate limit so page spamming doesn't saturate the MobiFlight websocket on weaker CPUs.
                elapsed = asyncio.get_running_loop().time() - last_run_time
                if elapsed < rate_limit_time:
                    await asyncio.sleep(rate_limit_time - elapsed)

                await websocket.send(generate_display_json(device, values))
                last_run_time = asyncio.get_running_loop().time()

            except websockets.exceptions.ConnectionClosed:
                logging.error("MobiFlight websocket connection was closed... Attempting to reconnect")
                await queue.put(values)
                break


async def handle_dataref_updates(queue: asyncio.Queue, dataref_map: dict[int, str]):
    last_known_values = {}

    logging.info("Connecting to X-Plane websocket server")
    async for websocket in websockets.connect(BASE_WEBSOCKET_URI):
        logging.info("Connected successfully to X-Plane websocket server")
        try:
            await websocket.send(
                json.dumps(
                    {
                        "type": "dataref_subscribe_values",
                        "req_id": 1,
                        "params": {"datarefs": [{"id": id_value} for id_value in dataref_map]},
                    }
                )
            )
            while True:
                data = json.loads(await websocket.recv())

                if "data" not in data:
                    continue

                new_values = dict(last_known_values)

                for dataref_id, value in data["data"].items():
                    dataref_name = dataref_map.get(int(dataref_id))
                    if dataref_name is None:
                        continue

                    raw = base64.b64decode(value)
                    if "/text_line" in dataref_name:
                        new_values[dataref_name] = raw.decode("utf-8", errors="replace").replace("\x00", " ")
                    elif "/style_line" in dataref_name:
                        new_values[dataref_name] = raw

                if new_values == last_known_values:
                    continue

                last_known_values = new_values
                await queue.put(new_values)
        except websockets.exceptions.ConnectionClosed:
            logging.error("X-Plane websocket connection was closed... Attempting to reconnect")
            continue


async def get_available_devices() -> list[CduDevice]:
    available_devices = []

    logging.info("Checking MobiFlight for available CDU devices")
    for device in CduDevice:
        device_endpoint = device.get_endpoint()
        try:
            async with websockets.connect(device_endpoint):
                logging.info("Discovered CDU device %s at endpoint %s", device, device_endpoint)
                available_devices.append(device)
        except (websockets.WebSocketException, OSError):
            logging.warning(
                "Attempted to probe CDU device %s at endpoint %s but device wasn't available",
                device,
                device_endpoint,
            )

    return available_devices


async def main():
    logging.basicConfig(
        level=os.environ.get("LOGLEVEL", "WARNING").upper(),
        format="%(levelname)s:%(message)s",
    )

    tasks = []

    for device in await get_available_devices():
        dataref_map = fetch_dataref_mapping(device)
        if not dataref_map:
            logging.warning("No MCDU datarefs found for device %s - is the DWSim ATR 72-600 loaded?", device)
            continue

        queue = asyncio.Queue()
        tasks.append(asyncio.create_task(handle_dataref_updates(queue, dataref_map)))
        tasks.append(asyncio.create_task(handle_device_update(queue, device)))

    logging.info("Started %d background tasks", len(tasks))
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
