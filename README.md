# WinWing Airbus Hardware Profiles for X-Plane (MobiFlight)

MobiFlight profiles that map **WinWing Airbus-style hardware** to non-Airbus aircraft add-ons in X-Plane 12.

## Hardware

These profiles are built for the following WinWing panels:

- **FCU-320** (Flight Control Unit)
- **EFIS-320L** (Electronic Flight Instrument System, Captain side)
- **MCDU-32 Captain** (Multi-Function Control & Display Unit)
- **AGP** (Autobrake & Gear Panel) — Falcon 8X profile only

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

## Aerobask Falcon 8X (`aerobask-falcon-8x/`)

**Aircraft:** [Aerobask Falcon 8X](https://www.aerobask.com/) (X-Plane 12)

The Falcon 8X has a Guidance Panel (GP) instead of an MCP/FCU, and its EASy displays are driven from the MKB/CCD rather than an EFIS panel. The aircraft logic is encrypted (SASL), so all commands and datarefs below were taken from the cockpit manipulators and validated against the running sim.

### What's Mapped

**196 total config items** (67 outputs, 129 inputs) across 3 devices: FCU-320 + EFIS-320L, MCDU-32 Captain, and AGP. Device names and button ids were checked against MobiFlight's WinWing definitions (`Joysticks/winwing/*.joystick.json` and `src/MobiFlightWwFcu/WinCtrl*Controller.cs`).

#### FCU → Guidance Panel — 25 inputs

| FCU Control | Falcon 8X Function | Command |
|-------------|--------------------|---------|
| SPD knob | Speed target | `aerobask/otto/spd_up` / `spd_dn` |
| SPD push / pull | Speed FMS / MAN | `aerobask/otto/at_man_fms_fms` / `_man` |
| SPD/MACH | KTS/MACH toggle | `sim/autopilot/knots_mach_toggle` |
| HDG knob | Heading/track target | `sim/autopilot/heading_up` / `heading_down` |
| HDG push / pull | HDG SYNC / HDG mode | `sim/autopilot/heading_sync` / `heading` |
| TRK/FPA | HDG/TRK selector | `aerobask/otto/hdg_trk` |
| LOC | LNAV | `aerobask/otto/ap_nav` |
| APPR | APP | `aerobask/otto/ap_app` |
| ALT knob | Altitude target | `sim/autopilot/altitude_up` / `altitude_down` |
| ALT push / pull | VNAV / CLB | `sim/autopilot/vnav` / `level_change` |
| ALT 100 / 1000 | ALT FT selector | `aerobask/otto/hun_tho_hun` / `hun_tho_tho` |
| V/S knob | VS/PATH thumbwheel | `sim/autopilot/vertical_speed_up` / `_down` |
| V/S push / pull | ALT hold / VS mode | `sim/autopilot/altitude_hold` / `vertical_speed` |
| AP1, AP2 | AP engage/disengage | `sim/autopilot/servos_toggle` |
| A/THR | AT engage/disengage | `sim/autopilot/autothrottle_toggle` |

**Outputs:**
- **SPD:** dashes in FMS speed mode (as on the real GP); in MAN, the selected speed or Mach from `sim/cockpit2/autopilot/airspeed_dial_kts_mach`.
- **HDG:** the Falcon publishes no dataref for its selected heading, so the window shows a value tracked by MobiFlight. It shows dashes until you **push the HDG knob** (HDG SYNC, which also sets the tracked value to the current heading); after that each knob click moves it ±1°. Heading changes made with the mouse in the cockpit are not seen, so push the knob again to re-sync.
- **ALT:** the ASEL from `aerobask/otto/knob_alt_sel` (ASEL ÷ 100, wrapping at 360, so FL370 reads 10). For ASEL of 36,000 ft and above, `sim/cockpit2/autopilot/altitude_dial_ft` is used to pick between the two candidates.
- **V/S:** dashes unless VS mode is active.
- **Dots:** SPD = FMS speed, HDG = LNAV armed/active, ALT = VNAV armed/active.
- **LEDs** (from `aerobask/otto/lit_*`): AP1 = AP, A/THR = AT, LOC = LNAV, APPR = APP.
- **Brightness:** gated on DC bus power; the backlight follows the GP panel-lights knob.

#### EFIS-320L — 23 inputs + 4 outputs

| EFIS Control | Falcon 8X Function | Dataref/Command |
|--------------|--------------------|-----------------|
| FD (33) | FD/TD pilot (cycles FD → TD → FD+TD → OFF) | `aerobask/otto/fd_td_pilot` |
| BARO push / pull (40/41) | STD on / off | `aerobask/baro/std_pilot` (gated on `aerobask/baro/1/is_std`) |
| BARO knob (42/43) | Pilot baro setting | `sim/instruments/barometer_down` / `_up` |
| inHg / hPa (44/45) | Pilot baro unit | `aerobask/baro/1/is_inhg` = 1 / 0 |
| CSTR (35) | MKB: CRS edit | `aerobask/mkb/left/goto_crs` |
| WPT (36) | MKB: DIRECT-TO | `aerobask/mkb/left/goto_dirto` |
| VOR.D (37) | MKB: NAV page | `aerobask/mkb/left/goto_nav` |
| NDB (38) | MKB: TRFC page | `aerobask/mkb/left/goto_trfc` |
| ARPT (39) | MKB: SHOW window | `aerobask/mkb/left/goto_show` |
| ND mode (46–50) | *Unverified* | `sim/cockpit2/EFIS/map_mode` |
| ND range (51–56) | *Unverified* | `sim/cockpit2/EFIS/map_range` |

**Outputs:** FD LED (FD/TD on); QNH in inHg or hPa following the aircraft's own unit setting, and "Std" when STD is selected.

#### MCDU → MKB (left multifunction keyboard) — 63 inputs

The Falcon's EASy FMS has no CDU screen (flight plans live on the MDU, driven by the cursor), so the MCDU acts as the **MKB keyboard** and its screen stays blank. All keys send `aerobask/mkb/left/...` commands.

| MCDU Key | MKB Function |
|----------|--------------|
| A–Z, 0–9, `.`, `/`, SP | Same key |
| +/- | Minus |
| CLR | CLR/DEL |
| OVFY | ENTER |
| Blank L / Blank R | SHIFT / SWAP |
| ← / → | Cursor left / right |
| LSK 1L–6L | VHF, NAV, XPDR, ATC, HF, SAT pages |
| LSK 1R–6R | CRS edit, DIRECT-TO, SHOW window, TRFC page, CHECKLIST window, XPDR IDENT |
| DIR / RAD NAV / ATC COMM | DIRECT-TO / NAV page / ATC page |
| MCDU MENU / AIRPORT | CHECKLIST window / SHOW window |

#### AGP (Autobrake & Gear Panel) — 14 inputs + 28 outputs

| AGP Control | Falcon 8X Function | Dataref/Command |
|-------------|--------------------|-----------------|
| Gear lever UP / DOWN | Landing gear | `sim/flight_controls/landing_gear_up` / `_down` |
| AUTO BRK LO | Taxi light toggle | `sim/lights/taxi_lights_toggle` |
| AUTO BRK MED | Both landing lights ON ↔ OFF | `aerobask/lights/ldg_left` / `ldg_right` = 2 / 0 |
| AUTO BRK MAX | Both landing lights PULSE ↔ OFF | `aerobask/lights/ldg_left` / `ldg_right` = 1 / 0 |
| A/SKID & N/W STRG ON / OFF | Nosewheel steering on / off (synced with the cockpit NWS button) | `sim/flight_controls/nwheel_steer_toggle` |
| CHR | Chrono start → stop → reset | `sim/instruments/chrono1_cycle` |
| RST | Chrono reset | `sim/instruments/chrono1_reset` |
| ET RUN / STP / RST | Elapsed timer run / stop / reset | `sim/instruments/elapsed1_start_stop` / `_reset` |

**Outputs:**
- **Gear lights:** green = down and locked, red UNLK = in transit (from `sim/flightmodel2/gear/deploy_ratio`; columns L / NOSE / R). The lever's red arrow uses `sim/cockpit2/annunciators/gear_unsafe`.
- **Lights:** LO is lit when the taxi light is on, MED when the landing lights are ON, and MAX while they are on PULSE. On PULSE, the green DECEL light above MAX also blinks, following the real left landing light (`sim/flightmodel2/lights/landing_lights_brightness_ratio[1]`), so it matches the Falcon's wig-wag rate (about 1.5 s per left/right cycle).
- **Clock:** UTC = sim zulu time, CHR = X-Plane chrono #1 (mm:ss), ET = X-Plane elapsed timer #1 (hh:mm). CHR and ET are blank when reset.
- **Brightness:** the backlight follows the GP panel-lights knob; LCD and LEDs are power-gated.

### Not Mapped / Limitations

| Item | Reason |
|------|--------|
| EXPED (7), METRIC (8), LS (34), NAV source selectors (57–62) | No natural Falcon 8X equivalent |
| ND mode / range | The EASy PDU format and range live in encrypted SASL code; mapped to the X-Plane generic EFIS datarefs, which may have no effect |
| VS/FPA (PATH) display | V/S window always shows ft/min |
| HDG window | Tracked value, not read from the aircraft (see Outputs). Re-sync with an HDG knob push after using the mouse |
| MCDU screen, PROG/PERF/INIT/DATA/F-PLN/FUEL PRED/SEC F-PLN, ↑/↓, BRT/DIM | EASy has no CDU page equivalent |
| Autobrake | The Falcon 8X has no autobrake, so the AUTO BRK buttons drive the taxi and landing lights instead |
| Landing lights | Driven through `aerobask/lights/ldg_left` / `ldg_right` (0 = OFF, 1 = PULSE, 2 = ON). The `sw_landing_*` datarefs are only the switch animation and ignore writes |
| AGP CHR/ET vs. the Falcon's own PDU timer | The AGP uses X-Plane's chrono/elapsed timers; the Falcon's ET button (`aerobask/easy/et_left`) keeps its own timer |
| BRK FAN, TERR ON ND, DATE, UTC selector, clock set knobs | No Falcon 8X equivalent |

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
