# Product Requirements Document: Piping Estimator

## Problem Statement

Mechanical engineers specializing in piping systems spend 4+ hours per estimate manually:
- Reading hundreds of pages of technical drawings (PDFs)
- Extracting pipe specifications (diameters, lengths, materials, fittings)
- Measuring pipe runs from isometric/schematic drawings
- Calculating quantities for fittings, valves, supports
- Creating itemized cost estimates

**Pain Point:** This manual process is time-consuming, error-prone, and bottlenecks the business.

---

## User Persona

**Name:** Piping Engineer (Company of One)  
**Specialization:** Mechanical engineering, industrial piping systems  
**Current Workflow:**
1. Receive PDF drawing package (100-500 pages)
2. Manually review each drawing to identify pipe runs
3. Extract specifications (pipe size, schedule, material, length)
4. Identify and count fittings (elbows, tees, reducers, valves, flanges)
5. Calculate material quantities
6. Apply unit costs and labor rates
7. Generate estimate document

**Time:** 4-8 hours per estimate  
**Error Rate:** High (missed items, measurement errors, incorrect counts)

---

## Proposed Solution

**AI-Powered Piping Estimator** that automates the entire workflow:

### Phase 1: PDF Analysis (AI Vision)
- Upload PDF drawing package
- AI vision model (Claude Sonnet 4.5 / GPT-4V) analyzes each page
- Extract pipe specifications from drawings:
  - Pipe sizes (diameter, schedule, material)
  - Pipe lengths (from isometric drawings)
  - Fittings (type, size, quantity)
  - Valves, flanges, supports
  - Line numbers and service descriptions

### Phase 2: Measurement Engine
- Parse extracted specifications
- Calculate pipe lengths from drawings (pixel measurements → real units)
- Count fittings automatically
- Apply standard piping rules:
  - Add fitting allowances (e.g., weld gap, flange bolt length)
  - Calculate support spacing
  - Determine insulation requirements

### Phase 3: Estimate Generation
- Apply unit costs (materials + labor)
- Generate itemized estimate:
  - Bill of materials (BOM)
  - Labor hours breakdown
  - Total cost with markup
- Export to Excel/CSV/PDF

---

## Technical Approach

### Architecture

```
┌─────────────────┐
│  PDF Upload     │
│  (drawings)     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  AI Vision      │  ← Claude Sonnet 4.5 / GPT-4V
│  Analysis       │     - Read drawings
│                 │     - Extract specs
│                 │     - OCR text annotations
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Spec Parser    │
│  & Validator    │  ← Normalize extracted data
│                 │     - Validate pipe sizes
│                 │     - Check material codes
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Measurement    │
│  Engine         │  ← Calculate quantities
│                 │     - Pipe lengths
│                 │     - Fitting counts
│                 │     - Support spacing
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Cost Engine    │  ← Apply pricing
│                 │     - Material unit costs
│                 │     - Labor rates
│                 │     - Markup %
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Export         │
│  (Excel/PDF)    │  ← Generate estimate
└─────────────────┘
```

### Technology Stack

**Backend:**
- Python 3.11+
- FastAPI (REST API)
- LangChain (AI orchestration)
- Anthropic Claude API (vision + reasoning)
- OpenAI GPT-4V (fallback/comparison)
- PyMuPDF / pdf2image (PDF processing)
- Pillow (image manipulation)
- Pandas (data manipulation)

**Frontend (Optional MVP):**
- Streamlit (quick prototype) OR
- React + TypeScript (production)

**Database:**
- PostgreSQL (specs, estimates, pricing)
- Redis (processing queue for large PDFs)

**Deployment:**
- Docker + docker-compose
- Cloud: Railway / Render / Fly.io (easy deployment)

---

## Success Criteria

### MVP Success Metrics

1. **Time Savings:** Reduce estimate time from 4+ hours → 15-30 minutes
2. **Accuracy:** 95%+ accuracy on pipe spec extraction
3. **Completeness:** Capture 90%+ of fittings/components automatically
4. **Usability:** Engineer can use tool with <10 min training

### Business Impact

- **10x faster estimates** → more bids, more revenue
- **Reduced errors** → fewer change orders, better margins
- **Competitive advantage** → faster turnaround wins more contracts

---

## MVP Scope (Phase 1)

### In Scope

✅ **Core Features:**
1. PDF upload (single drawing or multi-page package)
2. AI vision analysis of drawings
3. Extract pipe specifications:
   - Pipe size, schedule, material
   - Approximate lengths (from scale)
   - Fitting types and counts
4. Generate basic Bill of Materials (BOM)
5. Export BOM to CSV/Excel

✅ **Supported Drawing Types:**
- Isometric piping drawings (P&IDs)
- Piping schematics with annotations
- Standard engineering drawing formats

✅ **Supported Pipe Standards:**
- ASME/ANSI pipe sizes (NPS)
- Common materials (carbon steel, stainless, PVC)
- Standard schedules (Sch 40, Sch 80, etc.)

### Out of Scope (Future Enhancements)

❌ **Not in MVP:**
- Cost estimation (Phase 2)
- Labor hour calculations (Phase 2)
- Advanced 3D drawing analysis (Phase 3)
- Integration with ERP/estimating software (Phase 3)
- Mobile app (Phase 4)
- Multi-user collaboration (Phase 4)

---

## User Stories

### Epic 1: PDF Upload & Processing

**US-001:** As an engineer, I want to upload a PDF drawing package so that the system can analyze it.

**Acceptance Criteria:**
- Upload single PDF or ZIP of multiple PDFs
- System validates file format
- Shows upload progress
- Confirms successful upload

---

**US-002:** As an engineer, I want the system to automatically detect drawing pages so I don't have to manually select them.

**Acceptance Criteria:**
- System identifies piping drawings vs cover pages/notes
- Skips blank pages and non-technical content
- Shows list of detected drawings

---

### Epic 2: AI Vision Analysis

**US-003:** As an engineer, I want the AI to extract pipe specifications from drawings so I don't have to read them manually.

**Acceptance Criteria:**
- Extracts pipe sizes (diameter, schedule)
- Identifies material type
- Captures line numbers
- Detects service descriptions (e.g., "cooling water", "steam")

---

**US-004:** As an engineer, I want the AI to measure pipe lengths from drawings so I don't have to use a scale ruler.

**Acceptance Criteria:**
- Detects drawing scale (e.g., 1:50, 1/4"=1')
- Measures pipe runs in pixels
- Converts to real-world units (feet/meters)
- Provides confidence score for each measurement

---

**US-005:** As an engineer, I want the AI to identify and count fittings so I don't miss any components.

**Acceptance Criteria:**
- Detects elbows (90°, 45°), tees, reducers
- Identifies valves (gate, ball, check, globe)
- Counts flanges and unions
- Captures fitting sizes

---

### Epic 3: Bill of Materials Generation

**US-006:** As an engineer, I want the system to generate a Bill of Materials (BOM) so I can review the extracted specs.

**Acceptance Criteria:**
- BOM includes: item #, description, size, material, quantity
- Groups similar items (e.g., all 2" 90° elbows)
- Calculates total quantities
- Allows manual editing/corrections

---

**US-007:** As an engineer, I want to export the BOM to Excel so I can use it in my existing workflow.

**Acceptance Criteria:**
- Export to .xlsx format
- Includes all columns (item, description, qty, etc.)
- Formatted for readability
- Includes metadata (project name, date, engineer)

---

## Technical Requirements

### Functional Requirements

**FR-001:** System shall accept PDF files up to 100 MB  
**FR-002:** System shall process multi-page PDFs (up to 500 pages)  
**FR-003:** System shall extract text annotations using OCR  
**FR-004:** System shall analyze drawings using vision AI models  
**FR-005:** System shall detect drawing scale automatically  
**FR-006:** System shall convert pixel measurements to real-world units  
**FR-007:** System shall validate extracted specs against pipe standards  
**FR-008:** System shall generate BOM in structured format  
**FR-009:** System shall export BOM to Excel (.xlsx)  

### Non-Functional Requirements

**NFR-001:** System shall process a 100-page PDF in <5 minutes  
**NFR-002:** System shall achieve 95%+ accuracy on pipe spec extraction  
**NFR-003:** System shall provide confidence scores for all extractions  
**NFR-004:** System shall be usable by non-technical users  
**NFR-005:** System shall run on commodity hardware (8GB RAM, 4 cores)  

---

## Data Model

### Extracted Specifications (JSON)

```json
{
  "project": {
    "name": "Plant Expansion Project",
    "drawing_package": "P-001 to P-150",
    "date": "2026-02-15"
  },
  "drawings": [
    {
      "page": 5,
      "drawing_number": "P-042",
      "title": "Cooling Water Supply - Isometric",
      "scale": "1:50",
      "pipes": [
        {
          "line_number": "CW-101",
          "service": "Cooling Water Supply",
          "size": "4 inch",
          "schedule": "Sch 40",
          "material": "Carbon Steel",
          "length_ft": 125.5,
          "confidence": 0.95
        }
      ],
      "fittings": [
        {
          "type": "90° Elbow",
          "size": "4 inch",
          "material": "Carbon Steel",
          "quantity": 8,
          "confidence": 0.92
        },
        {
          "type": "Tee",
          "size": "4 inch",
          "material": "Carbon Steel",
          "quantity": 3,
          "confidence": 0.88
        }
      ],
      "valves": [
        {
          "type": "Gate Valve",
          "size": "4 inch",
          "material": "Carbon Steel",
          "quantity": 2,
          "confidence": 0.91
        }
      ]
    }
  ]
}
```

---

## Risks & Mitigations

### Technical Risks

**Risk 1:** AI vision models may struggle with low-quality scanned PDFs  
**Mitigation:** Pre-process images (enhance contrast, denoise), use multiple AI models for cross-validation

**Risk 2:** Drawing standards vary widely across companies  
**Mitigation:** Build configurable templates, allow user to define custom symbols/annotations

**Risk 3:** AI API costs could be high for large drawing packages  
**Mitigation:** Use smaller models for initial triage, only send relevant pages to expensive vision models

### Business Risks

**Risk 1:** Users may not trust AI-generated estimates  
**Mitigation:** Show confidence scores, allow manual review/editing, provide "AI-assisted" vs "fully automated" modes

**Risk 2:** Integration with existing workflows may be complex  
**Mitigation:** Start with simple CSV/Excel export, add integrations later

---

## Future Enhancements (Post-MVP)

### Phase 2: Cost Estimation
- Integrate pricing database (materials + labor)
- Calculate total project cost
- Apply markup/margin
- Generate customer-facing proposal

### Phase 3: Advanced Analysis
- 3D model parsing (STEP, IFC files)
- Support for P&ID diagrams (Process & Instrumentation)
- Equipment takeoff (pumps, tanks, heat exchangers)

### Phase 4: Collaboration & Workflow
- Multi-user access
- Version control for estimates
- Integration with ERP (Procore, Sage, QuickBooks)
- Mobile app for field verification

### Phase 5: Machine Learning
- Train custom model on user's historical drawings
- Learn company-specific symbols and standards
- Improve accuracy over time

---

## Open Questions

1. **Drawing Standards:** What specific piping standards does your friend use? (ASME, ISO, DIN?)
2. **Output Format:** What estimating software (if any) does he currently use?
3. **Pricing Data:** Does he have a materials pricing database, or should we integrate with vendors (Ferguson, McMaster-Carr)?
4. **Review Workflow:** Does he want to review/edit AI extractions before generating estimate, or trust fully automated output?
5. **Drawing Types:** Are most drawings isometric, P&ID, or orthographic (plan/elevation)?

---

## Success Definition

**MVP is successful if:**
- Your friend can upload a PDF drawing package
- System extracts 90%+ of pipe specs correctly
- BOM is generated in <5 minutes
- He can export to Excel and use it for estimates
- **He saves at least 3 hours per estimate**

---

## Timeline Estimate

**Phase 1 (MVP): 2-3 weeks**
- Week 1: PDF processing + AI vision integration
- Week 2: Spec extraction + measurement engine
- Week 3: BOM generation + Excel export + testing

**Phase 2 (Cost Estimation): 1-2 weeks**
- Pricing database integration
- Cost calculation engine
- Proposal generation

**Phase 3 (Production Deployment): 1 week**
- Dockerize app
- Deploy to cloud
- User training

---

## Next Steps

1. ✅ Create GitHub repository
2. ✅ Write PRD (this document)
3. ⏳ Break down into tasks
4. ⏳ Build proof-of-concept (single PDF → BOM)
5. ⏳ Test with real drawing samples from your friend
6. ⏳ Iterate based on feedback
7. ⏳ Deploy MVP

---

**Document Version:** 1.0  
**Last Updated:** 2026-02-15  
**Author:** Shelby (OpenClaw AI)
