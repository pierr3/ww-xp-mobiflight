# WinWing Airbus Hardware Profiles for X-Plane (MobiFlight)

MobiFlight profiles that map **WinWing Airbus-style hardware** to non-Airbus aircraft add-ons in X-Plane 12.

## Hardware

These profiles are built for the following WinWing panels:

- **FCU-320** (Flight Control Unit)
- **EFIS-320L** (Electronic Flight Instrument System, Captain side)
- **MCDU-32 Captain** (Multi-Function Control & Display Unit)

Since the hardware carries Airbus labeling (A320 FCU layout, Airbus MCDU function keys, etc.), buttons are remapped to the closest equivalent function on each Boeing/MD aircraft.

## Requirements

- [MobiFlight Connector](https://www.mobiflight.com/) — **latest beta version required** for MCDU support
- X-Plane 12
- The respective aircraft add-on (see below)
- WinWing FCU-320 + EFIS-320L and/or MCDU-32 Captain hardware

## Setup

1. Download the `.mfproj` file for your aircraft
2. Open MobiFlight Connector
3. Load the profile via **File > Open**
4. **Update the Module Serial numbers** to match your hardware — the serial values in these profiles are specific to the author's devices and will not match yours. In MobiFlight, go to each input/output config item and select your actual device from the dropdown, or do a find-and-replace in the `.mfproj` JSON file.

---

## FlightFactor Boeing 757 (`flightfactor-757/`)

**Aircraft:** [FlightFactor Boeing 757](https://store.x-plane.org/Boeing-757-v2-Professional_p_222.html) (FF76_75)

### What's Mapped

**147 total config items** (29 outputs, 118 inputs) across 3 devices.

#### FCU (Flight Control Unit) — 26 inputs + 16 outputs

| Control | Function | Type |
|---------|----------|------|
| SPD knob | IAS/Mach set, push/pull | Commands |
| HDG knob | Heading set, push/pull | Commands |
| ALT knob | Altitude set (100/1000 toggle), push/pull | Commands |
| VS knob | V/S set, push/pull | Commands |
| A/P 1 & 2 | Autopilot engage buttons | Commands |
| A/THR | Autothrottle toggle | Command |
| LOC | Localizer mode | Command |
| APPR | Approach mode | Command |
| EXPED | FLCH (Flight Level Change) mode | Command |
| Metric ALT | Meters display toggle | Command |
| SPD/Mach toggle | IAS/Mach switch | Command |

**Outputs (annunciators & displays):**
- SPD, HDG, ALT, V/S value displays
- AP1, AP2, A/THR, LOC, APPR, EXPED mode lamps
- SPD dash/dot, HDG dash/dot, V/S dash indicators
- Battery-gated brightness (displays blank when battery is off)

#### EFIS Panel — 23 inputs + 4 outputs

| Control | Function | Dataref/Command |
|---------|----------|-----------------|
| FD button (33) | Flight Director 1 toggle | `1-sim/command/AP/fd1Switcher_trigger` |
| CSTR (35) | FPV (Flight Path Vector) toggle | `1-sim/ndpanel/1/fpv` |
| WPT (36) | WPT map overlay toggle | `1-sim/ndpanel/1/map5` |
| VOR.D (37) | NAV AID / STA map overlay | `1-sim/ndpanel/1/map2` |
| NDB (38) | DATA map overlay | `1-sim/ndpanel/1/map4` |
| ARPT (39) | ARPT map overlay | `1-sim/ndpanel/1/map3` |
| BARO push (40) | Set STD barometric pressure | `1-sim/ng/baro/std/L` = 1 |
| BARO pull (41) | Exit STD baro | `1-sim/ng/baro/std/L` = 0 |
| BARO knob dec (42) | Decrease baro pressure | Command |
| BARO knob inc (43) | Increase baro pressure | Command |
| ND mode LS (46) | APP mode | `hsiModeRotary` = 1 |
| ND mode VOR (47) | VOR mode | `hsiModeRotary` = 0 |
| ND mode NAV (48) | MAP mode | `hsiModeRotary` = 2 |
| ND mode ARC (49) | MAP mode (duplicate) | `hsiModeRotary` = 2 |
| ND mode PLAN (50) | PLN mode | `hsiModeRotary` = 3 |
| ND range 10–320 (51–56) | Range selection | `hsiRangeRotary` = 1–6 |

#### MCDU (CDU) — 69 inputs + 9 outputs

All CDU button inputs write `1` to the `757Avionics/CDU/...` dataref (the FF757 plugin auto-resets to `0`).

| Control | 757 CDU Function |
|---------|-----------------|
| LSK 1L–6L | Line Select Keys Left (LLSK1–6) |
| LSK 1R–6R | Line Select Keys Right (RLSK1–6) |
| DIR | DIR |
| PROG | PROG |
| PERF | CLB (Climb) |
| INIT | INIT REF |
| DATA | CRZ (Cruise) |
| Blank R | EXEC (Execute) |
| F-PLN | RTE (Route) |
| RAD NAV | FIX |
| FUEL PRED | DES (Descent) |
| SEC F-PLN | LEGS |
| ATC COMM | HOLD |
| MCDU MENU | MCDU MENU |
| AIRPORT | DEP ARR |
| Blank L | DELETE |
| Left Arrow | PREV PAGE |
| Right Arrow | NEXT PAGE |
| A–Z, 0–9, ., +/-, /, SP, CLR | Direct mapping |

**MCDU Display:** Full 14-line CDU display on the WinWing MCDU screen (lines 0–13 with color support via the `1-sim/cduL/...` datarefs).

### Not Mapped / Limitations

| Button | Reason |
|--------|--------|
| LS (34) | No equivalent on 757 — ILS bars appear automatically in APP mode |
| inHg / hPa (44–45) | Real 757 has no baro unit toggle on EFIS panel |
| NAV source selectors (57–62) | VOR/ADF selector datarefs are encrypted in SASL plugin |
| BRT / DIM (19, 26) | CDU brightness — not mapped |
| Up / Down arrows (30, 32) | No 757 CDU equivalent |
| OVFY (73) | No 757 CDU equivalent |
| ND ARC mode | Maps to MAP (same as NAV) — 757 has no separate ARC mode |
| Map filter toggles | Write `1` to toggle ON; may need adjustment if they don't toggle OFF |

---

## Rotate MD-80 (`rotate-md80/`)

**Aircraft:** [Rotate MD-80](https://www.rotate.com/) (MD-80 series)

### What's Mapped

**145 total config items** (35 outputs, 110 inputs) across 2 devices.

#### FCU — Inputs + Outputs

| Control | Function | Notes |
|---------|----------|-------|
| SPD knob | IAS set, push/pull | Commands |
| HDG knob | Heading set, push/pull | Commands |
| ALT knob | Altitude set, push/pull | Commands |
| VS knob | V/S set, push/pull | Commands |
| A/P 1 & 2 | Autopilot engage | Commands |
| A/THR | Autothrottle toggle | Dual preconditioned writes (creative workaround) |
| LOC | Localizer mode | Command |
| APPR | Approach mode | Command |
| SPD/Mach toggle | IAS/Mach switch | Command |

**Outputs:** SPD, HDG, ALT, V/S displays with annunciator lamps.

#### EFIS Panel — Inputs + Outputs

| Control | Function |
|---------|----------|
| FD button | Flight Director toggle |
| ND mode selector | VOR/APP/MAP/PLN modes |
| ND range selector | Range steps |
| BARO push/pull | STD baro set/exit |
| BARO knob | Baro pressure adjust (uses pre-computed output values) |
| inHg / hPa toggle | Baro unit switch (uses MobiFlight internal variable) |
| Map filter buttons | ARPT, WPT, NAV AID, DATA overlays |

**Baro display:** Shows either inHg or hPa based on a MobiFlight variable toggle — a creative workaround since the MD-80 doesn't natively expose a unit toggle.

#### MCDU (CDU) — Full Mapping

| Control | MD-80 Function |
|---------|---------------|
| LSK 1L–6L, 1R–6R | Line Select Keys |
| Function keys | Mapped to MD-80 CDU equivalents |
| A–Z, 0–9, special keys | Direct mapping via `rotate/md80/cdu/Cdu_...` commands |

**MCDU Display:** Full CDU display output on the WinWing MCDU screen.

### Notable Implementation Details

- **A/THR Toggle:** The MD-80's autothrottle required a creative dual-preconditioned approach — two config items that check current state before writing, effectively creating a toggle from a non-toggle dataref.
- **Baro Adjustment:** Uses pre-computed MobiFlight output values fed back into input expressions for smooth baro knob operation.
- **inHg/hPa Display:** Implements a MobiFlight variable-based toggle to switch the baro display unit, since the MD-80 doesn't expose this as a simple dataref.

---

## Airbus-to-Boeing/MD Button Mapping Philosophy

Since the WinWing hardware has Airbus labels, here's the general remapping logic:

| Airbus Label | Boeing 757 | MD-80 |
|-------------|-----------|-------|
| DIR | DIR | DIR |
| PROG | PROG | PROG |
| PERF | CLB | CLB |
| INIT | INIT REF | INIT REF |
| DATA | CRZ | CRZ |
| F-PLN | RTE | RTE |
| RAD NAV | FIX | FIX |
| FUEL PRED | DES | DES |
| SEC F-PLN | LEGS | LEGS |
| ATC COMM | HOLD | HOLD |
| AIRPORT | DEP ARR | DEP ARR |
| ND LS mode | APP mode | APP mode |
| ND NAV mode | MAP mode | MAP mode |
| ND ARC mode | MAP mode | MAP mode |

## Troubleshooting

- **Buttons not responding:** Check that your Module Serial numbers match your actual hardware. The serials in these profiles are from the author's setup.
- **MCDU display not working:** Make sure you are running the latest MobiFlight beta. Stable releases do not yet support MCDU display output.
- **FCU displays blank:** Some profiles gate display brightness on the aircraft battery — make sure the aircraft is powered up.

## Contributing

Found a missing dataref or have a mapping improvement? Pull requests and issues are welcome.

## License

[MIT](LICENSE)
