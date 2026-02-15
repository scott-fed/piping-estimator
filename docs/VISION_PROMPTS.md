# AI Vision Prompts for Piping Extraction

## Prompt Engineering Strategy

### Goals
1. Extract structured data from piping drawings
2. High accuracy (95%+ target)
3. Confidence scores for each extraction
4. Handle variations in drawing styles

### Approach
- Use Claude Sonnet 4.5 (best vision model)
- Few-shot examples in prompts
- JSON schema for structured output
- Multi-pass extraction (classify → extract → validate)

---

## Prompt 1: Page Classification

**Purpose:** Identify which pages contain piping information

```markdown
You are analyzing a PDF page from an engineering drawing package.

Classify this page as one of the following:
- "piping_isometric": Isometric piping drawing with 3D representation
- "piping_plan": Plan view piping layout
- "piping_elevation": Elevation view piping
- "p&id": Process & Instrumentation Diagram
- "title_block": Cover page or title block only
- "notes": Specification or notes page
- "other": Non-piping content

Look for:
- Pipe symbols (lines with size annotations)
- Fittings (elbows, tees, valves)
- Line numbers (e.g., "CW-101", "ST-4-CS-201")
- Scale indicator (e.g., "1:50", "1/4\"=1'")
- Dimension lines and measurements

Return JSON:
{
  "page_type": "piping_isometric",
  "confidence": 0.95,
  "has_pipes": true,
  "has_scale": true,
  "scale": "1:50",
  "drawing_number": "P-042",
  "title": "Cooling Water Supply - Isometric"
}
```

---

## Prompt 2: Pipe Specification Extraction

**Purpose:** Extract pipe specs from a piping drawing

```markdown
You are extracting pipe specifications from an isometric piping drawing.

Extract ALL pipes visible in this drawing. For each pipe, identify:

1. **Line Number** - Format: [Service]-[Size]-[Material]-[Sequence]
   Examples: "CW-4-CS-101", "ST-2-304SS-201"

2. **Size** - Nominal Pipe Size (NPS) in inches
   Examples: "1/2\"", "2\"", "4\"", "6\""

3. **Schedule** - Wall thickness schedule
   Common: Sch 10, Sch 40, Sch 80, Sch 160

4. **Material** - Pipe material code
   Common: CS (carbon steel), SS (stainless 304), 316SS, A106-B

5. **Service** - What flows through the pipe
   Examples: "Cooling Water", "Steam", "Air", "Natural Gas"

6. **Length** - Approximate length in feet (if scale is visible)
   Use the scale indicator to convert pixel measurements

Return JSON array:
```json
{
  "pipes": [
    {
      "line_number": "CW-4-CS-101",
      "size": "4\"",
      "schedule": "Sch 40",
      "material": "Carbon Steel (A106-B)",
      "service": "Cooling Water Supply",
      "length_ft": 125.5,
      "confidence": 0.95,
      "notes": "Main supply line from pump"
    }
  ],
  "scale": "1:50",
  "units": "feet"
}
```

**Important:**
- If a spec is unclear, set confidence <0.70
- If length can't be measured (no scale), set to null
- Include all visible pipes, even short segments
```

---

## Prompt 3: Fitting Extraction

**Purpose:** Identify and count fittings

```markdown
You are identifying pipe fittings in an isometric piping drawing.

Extract ALL fittings visible. Look for these symbols:

**Elbows:**
- 90° elbow (right angle turn)
- 45° elbow (diagonal turn)
- Long radius (LR) or short radius (SR)

**Tees:**
- Straight tee (3-way connection)
- Reducing tee (different sizes)

**Reducers:**
- Concentric reducer (centered)
- Eccentric reducer (offset)

**Caps:**
- Pipe end caps

**Couplings & Unions:**
- Pipe connections

For each fitting, identify:
1. **Type** - 90° elbow, tee, reducer, etc.
2. **Size** - Pipe size(s) it connects
3. **Material** - Usually matches pipe material
4. **Quantity** - How many of this exact type/size

Return JSON:
```json
{
  "fittings": [
    {
      "type": "90° Elbow (LR)",
      "size": "4\"",
      "material": "Carbon Steel",
      "quantity": 8,
      "line_number": "CW-4-CS-101",
      "confidence": 0.92,
      "notes": "Standard butt-weld elbows"
    },
    {
      "type": "Tee",
      "size": "4\" x 2\"",
      "material": "Carbon Steel",
      "quantity": 2,
      "line_number": "CW-4-CS-101",
      "confidence": 0.88,
      "notes": "Reducing tee for branch connection"
    }
  ]
}
```

**Counting Rules:**
- Count each occurrence separately
- For identical fittings on same line, combine quantity
- If uncertain, estimate and set confidence <0.75
```

---

## Prompt 4: Valve Extraction

**Purpose:** Identify valves and actuators

```markdown
You are identifying valves in a piping drawing.

Look for these valve symbols:

**Gate Valve:**
- Rectangular symbol with gate wedge
- Used for on/off service

**Globe Valve:**
- Rounded body with internal disc
- Used for throttling

**Ball Valve:**
- Circle with ball inside
- Quarter-turn operation

**Check Valve:**
- Arrow showing flow direction
- Prevents backflow

**Butterfly Valve:**
- Disc rotating on shaft
- Common in large sizes

**Other:**
- Plug valve, needle valve, safety valve, etc.

For each valve, identify:
1. **Type** - Gate, globe, ball, check, etc.
2. **Size** - Pipe size
3. **Pressure Class** - 150, 300, 600, etc. (if shown)
4. **Operator** - Manual (hand wheel), electric, pneumatic, hydraulic
5. **Material** - Usually matches pipe

Return JSON:
```json
{
  "valves": [
    {
      "type": "Gate Valve",
      "size": "4\"",
      "pressure_class": "Class 150",
      "operator": "Manual (hand wheel)",
      "material": "Carbon Steel",
      "line_number": "CW-4-CS-101",
      "quantity": 2,
      "confidence": 0.91,
      "notes": "Isolation valves at pump discharge"
    }
  ]
}
```
```

---

## Prompt 5: Flange Extraction

**Purpose:** Identify flanges

```markdown
You are identifying flanges in a piping drawing.

Look for flange symbols:
- Welding neck (WN): Long tapered hub
- Slip-on (SO): Short hub
- Blind: Solid plate (no opening)
- Lap joint: Rotating flange with stub end

For each flange, identify:
1. **Type** - WN, SO, Blind, Lap Joint
2. **Size** - Pipe size
3. **Pressure Class** - 150, 300, 600, etc.
4. **Facing** - Raised face (RF), flat face (FF), ring-type joint (RTJ)

Return JSON:
```json
{
  "flanges": [
    {
      "type": "Weld Neck",
      "size": "4\"",
      "pressure_class": "Class 150",
      "facing": "Raised Face (RF)",
      "material": "Carbon Steel",
      "line_number": "CW-4-CS-101",
      "quantity": 4,
      "confidence": 0.89,
      "notes": "Equipment connections"
    }
  ]
}
```
```

---

## Prompt 6: Scale Detection

**Purpose:** Find drawing scale for measurements

```markdown
You are looking for the scale indicator on this engineering drawing.

Common locations:
- Title block (lower right corner)
- Near the drawing title
- In the notes section

Common formats:
- Ratio: "1:50", "1:100", "1:25"
- Architectural: "1/4\"=1'", "1/8\"=1'", "3/8\"=1'"
- Metric: "1:50 mm", "1:100 mm"

Also look for:
- Scale bar (graphical ruler)
- Dimension annotations

Return JSON:
```json
{
  "scale_found": true,
  "scale_format": "1:50",
  "scale_type": "ratio",
  "units": "millimeters",
  "confidence": 0.98,
  "location": "title block",
  "notes": "Scale applies to main drawing only, not details"
}
```

If no scale found:
```json
{
  "scale_found": false,
  "confidence": 0.95,
  "notes": "No scale indicator visible. May be 'NTS' (Not To Scale)"
}
```
```

---

## Prompt 7: Complete Drawing Analysis (All-in-One)

**Purpose:** Extract everything in one pass

```markdown
You are analyzing an isometric piping drawing to extract specifications for cost estimation.

Extract ALL of the following:

1. **Drawing Info:**
   - Drawing number
   - Title
   - Scale
   - Revision

2. **Pipes:**
   - Line number, size, schedule, material, service, length

3. **Fittings:**
   - Type, size, material, quantity

4. **Valves:**
   - Type, size, class, operator, material, quantity

5. **Flanges:**
   - Type, size, class, facing, material, quantity

6. **Other Components:**
   - Strainers, traps, instruments, specialty items

7. **Supports:**
   - Estimate support quantity based on pipe length
   - Use 10-20 ft spacing guideline

Return comprehensive JSON:
```json
{
  "drawing": {
    "number": "P-042",
    "title": "Cooling Water Supply - Isometric",
    "scale": "1:50",
    "revision": "B",
    "date": "2025-01-15"
  },
  "pipes": [...],
  "fittings": [...],
  "valves": [...],
  "flanges": [...],
  "instruments": [...],
  "supports": {
    "clamps": 12,
    "hangers": 5,
    "shoes": 0,
    "confidence": 0.80,
    "notes": "Estimated based on pipe length and spacing guidelines"
  },
  "overall_confidence": 0.91,
  "extraction_notes": [
    "High quality drawing, clear annotations",
    "All specifications visible and legible",
    "Minor uncertainty on 2 reducer sizes"
  ]
}
```

**Accuracy Guidelines:**
- High confidence (>0.90): Clear, unambiguous
- Medium confidence (0.70-0.90): Readable but some uncertainty
- Low confidence (<0.70): Unclear, estimate, or missing info

**For missing specs:**
- Set field to null
- Set confidence <0.70
- Add note explaining what's missing

**Quality checks:**
- Do fitting sizes match pipe sizes?
- Are materials consistent on same line?
- Do valve counts make sense?
- Is total pipe length reasonable?
```

---

## Example Few-Shot Prompts

### Example 1: Clear 4" Pipe

**Input:** [Image of clear piping isometric]

**Expected Output:**
```json
{
  "pipes": [
    {
      "line_number": "CW-4-CS-101",
      "size": "4\"",
      "schedule": "Sch 40",
      "material": "A106-B Carbon Steel",
      "service": "Cooling Water Supply",
      "length_ft": 125.5,
      "confidence": 0.97
    }
  ]
}
```

### Example 2: Unclear Material

**Input:** [Image where material annotation is partially obscured]

**Expected Output:**
```json
{
  "pipes": [
    {
      "line_number": "ST-2-???-201",
      "size": "2\"",
      "schedule": "Sch 80",
      "material": null,
      "service": "Steam",
      "length_ft": 42.0,
      "confidence": 0.68,
      "notes": "Material annotation unclear, likely carbon steel based on service"
    }
  ]
}
```

---

## Prompt Optimization Tips

### For Better Accuracy

1. **Be Specific:**
   - Define exact JSON schema
   - Give examples of good and bad outputs
   - Specify units (feet, meters, inches)

2. **Set Confidence Thresholds:**
   - >0.90 = Auto-accept
   - 0.70-0.90 = Flag for review
   - <0.70 = Requires manual verification

3. **Handle Edge Cases:**
   - Partially visible pipes
   - Blurry scans
   - Handwritten annotations
   - Non-standard symbols

4. **Multi-Model Validation:**
   - Run same image through Claude + GPT-4V
   - Compare results
   - Flag discrepancies

5. **Iterative Refinement:**
   - Start with sample drawings
   - Measure accuracy
   - Adjust prompts based on errors
   - Repeat

### Prompt Versioning

Track prompt versions and performance:

```json
{
  "prompt_version": "1.0",
  "model": "claude-sonnet-4-5",
  "date": "2026-02-15",
  "accuracy_test_results": {
    "pipe_specs": 0.95,
    "fittings": 0.92,
    "valves": 0.91,
    "overall": 0.93
  },
  "notes": "Initial version, tested on 10 sample drawings"
}
```

---

## Testing Checklist

Before deploying prompts:

- [ ] Test on 5+ sample drawings
- [ ] Measure accuracy vs manual extraction
- [ ] Check confidence scores correlate with errors
- [ ] Verify JSON schema is correct
- [ ] Test edge cases (poor quality, complex drawings)
- [ ] Compare Claude vs GPT-4V results
- [ ] Time the extraction (should be <30 sec/page)
- [ ] Review false positives/negatives

---

## Next Steps

1. ✅ Prompts defined
2. ⏳ Test with synthetic/public drawings
3. ⏳ Refine based on test results
4. ⏳ Test with friend's real drawings when available
5. ⏳ Fine-tune for his specific drawing style
6. ⏳ Deploy in production

---

**These prompts are ready to test as soon as we have sample drawings!**
