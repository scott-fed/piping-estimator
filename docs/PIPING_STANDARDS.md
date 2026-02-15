# Piping Standards Reference

## Overview

This document covers the key piping standards used in mechanical engineering for estimation and design.

---

## ASME B31.3 - Process Piping

**Scope:** Design, materials, fabrication, assembly, erection, examination, inspection, and testing of piping for petroleum refineries, chemical plants, and related processing facilities.

### Key Specifications

**Pipe Sizes (NPS - Nominal Pipe Size):**
- Small bore: 1/2" to 2"
- Medium bore: 2-1/2" to 12"
- Large bore: 14" and above

**Common Pipe Schedules:**
- **Schedule 10:** Thin wall (low pressure)
- **Schedule 40:** Standard wall (most common)
- **Schedule 80:** Extra strong wall
- **Schedule 160:** Extra extra strong wall

**Wall Thickness Calculation:**
```
t = (P × D) / (2 × (S × E + P × Y))

Where:
t = Wall thickness (inches)
P = Internal design pressure (psi)
D = Outside diameter (inches)
S = Allowable stress (psi)
E = Weld joint efficiency factor
Y = Temperature coefficient
```

---

## ASME B16.9 - Factory-Made Wrought Butt-Welding Fittings

**Covers:** Dimensions and tolerances for pipe fittings

### Fitting Types

**Elbows:**
- 90° long radius (LR) - Most common, R = 1.5D
- 90° short radius (SR) - R = 1.0D
- 45° elbow - For gentle direction changes

**Tees:**
- Straight tee - Equal or reducing
- Branch connection at 90°

**Reducers:**
- Concentric reducer - Centered
- Eccentric reducer - Offset (drainage/no pockets)

**Caps:**
- End caps for pipe termination

### Standard Dimensions (Examples)

**90° Long Radius Elbow (Sch 40):**
- 2" NPS: Center-to-face = 3.00", Approx weight = 0.47 lbs
- 4" NPS: Center-to-face = 6.00", Approx weight = 2.70 lbs
- 6" NPS: Center-to-face = 9.00", Approx weight = 7.50 lbs
- 8" NPS: Center-to-face = 12.00", Approx weight = 16.00 lbs

**Tee Dimensions (Sch 40):**
- 2" NPS: Center-to-end = 3.00", Approx weight = 0.66 lbs
- 4" NPS: Center-to-end = 6.00", Approx weight = 4.70 lbs
- 6" NPS: Center-to-end = 9.00", Approx weight = 13.50 lbs

---

## ASME B16.5 - Pipe Flanges and Flanged Fittings

**Covers:** Flange types, dimensions, bolt patterns, pressure ratings

### Flange Types

**Welding Neck (WN):**
- Best for high pressure/temperature
- Long tapered hub, butt-welded
- Most expensive

**Slip-On (SO):**
- Lower cost than WN
- Slips over pipe, fillet welded
- Lower pressure rating

**Blind Flange:**
- Closes end of pipe
- Used for inspection access

**Lap Joint:**
- Used with stub ends
- Rotating flange for bolt hole alignment

**Threaded:**
- Screwed onto pipe
- No welding required
- Limited pressure rating

### Pressure Classes

- **Class 150:** Up to 285 psi @ ambient temp
- **Class 300:** Up to 740 psi @ ambient temp
- **Class 600:** Up to 1480 psi @ ambient temp
- **Class 900:** Up to 2220 psi @ ambient temp
- **Class 1500:** Up to 3705 psi @ ambient temp
- **Class 2500:** Up to 6170 psi @ ambient temp

### Flange Dimensions (Class 150, WN)

**2" NPS:**
- Outside diameter: 6.00"
- Bolt circle: 4.75"
- Bolts: 4 × 5/8"
- Thickness: 0.62"

**4" NPS:**
- Outside diameter: 9.00"
- Bolt circle: 7.50"
- Bolts: 8 × 5/8"
- Thickness: 0.94"

**6" NPS:**
- Outside diameter: 11.00"
- Bolt circle: 9.50"
- Bolts: 8 × 3/4"
- Thickness: 1.00"

---

## Common Pipe Materials

### Carbon Steel

**ASTM A106:**
- Seamless carbon steel pipe
- Grades: A (tensile 48K), B (60K), C (70K)
- Most common: Grade B
- Temperature: -29°F to 750°F

**ASTM A53:**
- Black and hot-dipped galvanized
- Grades: A (tensile 48K), B (60K)
- Type E (ERW), Type S (Seamless)

**ASTM A333:**
- Low-temperature service
- Grades 1, 3, 6, 7, 8, 9, 10, 11
- Down to -150°F

### Stainless Steel

**ASTM A312:**
- Seamless and welded austenitic stainless
- Grade 304/304L (most common)
- Grade 316/316L (higher corrosion resistance)

**ASTM A358:**
- Electric-fusion-welded austenitic chromium-nickel
- Large diameter (24"+)

### Alloys

**ASTM B161/B162:**
- Nickel and nickel-copper (Monel)
- Corrosive environments

**ASTM B165/B167:**
- Nickel-chromium-iron (Inconel)
- High temperature

---

## Pipe Schedules Reference Table

| NPS  | Sch 10 | Sch 40 | Sch 80 | Sch 160 |
|------|--------|--------|--------|---------|
| 1/2" | 0.065" | 0.109" | 0.147" | 0.188"  |
| 3/4" | 0.065" | 0.113" | 0.154" | 0.219"  |
| 1"   | 0.065" | 0.133" | 0.179" | 0.250"  |
| 2"   | 0.065" | 0.154" | 0.218" | 0.343"  |
| 4"   | 0.083" | 0.237" | 0.337" | 0.531"  |
| 6"   | 0.109" | 0.280" | 0.432" | 0.719"  |
| 8"   | 0.109" | 0.322" | 0.500" | 0.906"  |
| 10"  | 0.134" | 0.365" | 0.593" | 1.125"  |
| 12"  | 0.156" | 0.375" | 0.687" | 1.312"  |

Note: Wall thickness in inches

---

## Valve Types

### Gate Valve
- Full flow, minimal pressure drop
- On/off service (not for throttling)
- Rising or non-rising stem

### Globe Valve
- Throttling service
- Higher pressure drop
- Good shutoff

### Ball Valve
- Quick on/off (1/4 turn)
- Low pressure drop
- Excellent shutoff

### Check Valve
- Prevents backflow
- Types: swing, lift, tilting disc
- Automatic operation

### Butterfly Valve
- Lightweight, compact
- Throttling or on/off
- Low cost for large sizes

### Plug Valve
- Quick on/off
- Multi-port available
- High torque

---

## Support Spacing Guidelines (ASME B31.3)

Maximum span between supports (carbon steel, water-filled):

| NPS   | Max Span (ft) |
|-------|---------------|
| 1"    | 7             |
| 2"    | 10            |
| 3"    | 12            |
| 4"    | 14            |
| 6"    | 17            |
| 8"    | 19            |
| 10"   | 22            |
| 12"   | 23            |
| 16"   | 27            |
| 20"   | 30            |

**Note:** Reduce by 10% for steam service

---

## Fitting Allowances for Takeoff

When calculating pipe lengths, add these allowances:

**Butt-Weld Fittings:**
- No additional length (already in center-to-face dimension)
- Weld gap: 1/16" to 1/8" (usually negligible)

**Socket-Weld Fittings:**
- Socket depth minus 1/16" expansion gap
- Typical: 1" depth - 1/16" = 15/16"

**Threaded Fittings:**
- Thread engagement: ~1/2" for 1", ~3/4" for 2", ~1" for 4"

**Flanges:**
- Flange face to weld bevel
- Add gasket thickness (1/16" typical)
- Bolt length calculation (thickness + gasket + nut)

---

## Insulation Considerations

**Pipe Insulation Thickness (Hot Service, 350°F):**

| NPS   | Thickness |
|-------|-----------|
| 1"-3" | 1.5"      |
| 4"-6" | 2.0"      |
| 8"-12"| 2.5"      |
| 14"+  | 3.0"      |

**Cold Service (<40°F):**
- Add vapor barrier
- Increase thickness by 50%

---

## Weight Estimation

**Pipe Weight (lbs/ft) - Carbon Steel Sch 40:**

| NPS | Weight |
|-----|--------|
| 1"  | 1.68   |
| 2"  | 3.65   |
| 4"  | 10.79  |
| 6"  | 18.97  |
| 8"  | 28.55  |
| 10" | 40.48  |
| 12" | 49.56  |

**Water Weight (lbs/ft):**

| NPS | Weight |
|-----|--------|
| 2"  | 1.04   |
| 4"  | 4.33   |
| 6"  | 9.34   |
| 8"  | 16.39  |
| 10" | 26.62  |
| 12" | 37.57  |

---

## AI Vision Extraction Targets

When analyzing piping drawings, extract:

1. **Pipe Specifications:**
   - Size (NPS or DN)
   - Schedule (10, 40, 80, etc.)
   - Material (A106-B, 304SS, etc.)
   - Service (steam, water, air, etc.)
   - Line number (CW-101, etc.)

2. **Fittings:**
   - Type (90° elbow, tee, reducer, etc.)
   - Size (matching pipe or reducing)
   - Material (usually matches pipe)
   - Quantity

3. **Valves:**
   - Type (gate, globe, ball, check, etc.)
   - Size
   - Pressure rating (Class 150, 300, etc.)
   - Operator (manual, electric, pneumatic)

4. **Flanges:**
   - Type (WN, SO, blind, etc.)
   - Size
   - Pressure class
   - Facing (RF, FF, RTJ)

5. **Specialty Items:**
   - Strainers
   - Traps (steam)
   - Expansion joints
   - Instruments (pressure gauges, thermometers)

6. **Supports:**
   - Type (hanger, clamp, shoe, guide)
   - Quantity (based on span)

---

## Common Drawing Annotations

**Line Number Format:**
`[Service Code]-[Size]-[Material]-[Sequence]`

Example: `CW-4-CS-101`
- CW = Cooling Water
- 4 = 4" NPS
- CS = Carbon Steel
- 101 = Line sequence number

**Service Codes:**
- CW = Cooling Water
- FW = Fire Water
- DW = Domestic Water
- ST = Steam
- CN = Condensate
- IA = Instrument Air
- PA = Plant Air
- NG = Natural Gas

**Material Codes:**
- CS = Carbon Steel
- SS = Stainless Steel (304)
- 316SS = Stainless Steel (316)
- PVC = PVC Plastic
- CPVC = CPVC Plastic

---

## References

- ASME B31.3: Process Piping
- ASME B16.9: Factory-Made Wrought Butt-Welding Fittings
- ASME B16.5: Pipe Flanges and Flanged Fittings
- ASTM Standards: Material specifications
- Pipe Data Handbook (Mohinder L. Nayyar)
- Piping Handbook (Mohinder L. Nayyar)
- Cameron Hydraulic Data Book

---

**Note:** This is a reference guide for AI vision prompt engineering and BOM validation. Always verify against current ASME/ASTM standards for production use.
