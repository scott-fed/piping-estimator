# Piping Estimator - Task List

## Project Phases

- **Phase 1:** MVP - PDF to BOM (2-3 weeks)
- **Phase 2:** Cost Estimation (1-2 weeks)
- **Phase 3:** Production Deployment (1 week)

---

## Phase 1: MVP - PDF to BOM

### Epic 1: Project Setup & Infrastructure

**TASK-001: Initialize Project Structure**
- [ ] Create Python project structure (src/, tests/, docs/)
- [ ] Set up virtual environment (Python 3.11+)
- [ ] Create requirements.txt with core dependencies
- [ ] Set up .gitignore for Python projects
- [ ] Create docker-compose.yml for local development
- **Estimate:** 1 hour

**TASK-002: Configure AI API Clients**
- [ ] Set up Anthropic Claude API credentials
- [ ] Set up OpenAI API credentials (fallback)
- [ ] Create environment variable config (.env.example)
- [ ] Write API client wrappers (rate limiting, error handling)
- [ ] Test API connectivity
- **Estimate:** 2 hours

**TASK-003: Set Up FastAPI Backend**
- [ ] Create FastAPI app structure
- [ ] Configure CORS for frontend access
- [ ] Set up health check endpoint
- [ ] Add request logging middleware
- [ ] Create Pydantic models for request/response
- **Estimate:** 2 hours

**TASK-004: Set Up Database (PostgreSQL)**
- [ ] Create docker-compose service for PostgreSQL
- [ ] Design database schema (projects, drawings, specs, estimates)
- [ ] Set up SQLAlchemy models
- [ ] Create Alembic migrations
- [ ] Write database initialization script
- **Estimate:** 3 hours

---

### Epic 2: PDF Processing & Upload

**TASK-005: Implement PDF Upload Endpoint**
- [ ] Create POST /api/upload endpoint
- [ ] Validate file type (PDF only)
- [ ] Validate file size (<100 MB)
- [ ] Save uploaded file to storage (local or S3)
- [ ] Return upload confirmation with file ID
- **Estimate:** 2 hours

**TASK-006: Build PDF Parser**
- [ ] Install PyMuPDF (fitz) library
- [ ] Extract text from PDF pages using OCR
- [ ] Convert PDF pages to images (for AI vision)
- [ ] Detect drawing scale from text annotations
- [ ] Handle multi-page PDFs efficiently
- **Estimate:** 4 hours

**TASK-007: Implement Page Classification**
- [ ] Use AI to classify pages (drawing vs cover/notes)
- [ ] Identify piping drawings vs other technical docs
- [ ] Skip blank pages automatically
- [ ] Return list of relevant pages for analysis
- **Estimate:** 3 hours

**TASK-008: Image Preprocessing**
- [ ] Enhance image contrast for better AI recognition
- [ ] Denoise scanned drawings
- [ ] Rotate images to correct orientation
- [ ] Resize images for optimal AI processing
- **Estimate:** 2 hours

---

### Epic 3: AI Vision Integration

**TASK-009: Build Vision Prompt Templates**
- [ ] Write prompt for pipe spec extraction
- [ ] Write prompt for fitting identification
- [ ] Write prompt for measurement extraction
- [ ] Include few-shot examples in prompts
- [ ] Create prompt versioning system
- **Estimate:** 3 hours

**TASK-010: Integrate Claude Vision API**
- [ ] Send drawing images to Claude 4.5 Sonnet
- [ ] Parse JSON responses from vision model
- [ ] Handle API errors and retries
- [ ] Implement rate limiting (avoid throttling)
- [ ] Log all API calls for debugging
- **Estimate:** 4 hours

**TASK-011: Implement Multi-Model Validation**
- [ ] Send same drawing to Claude + GPT-4V
- [ ] Compare results for discrepancies
- [ ] Use consensus for higher confidence
- [ ] Flag low-confidence extractions for manual review
- **Estimate:** 3 hours

**TASK-012: Build Confidence Scoring System**
- [ ] Calculate confidence scores for each extraction
- [ ] Use model-provided confidence when available
- [ ] Implement cross-validation scoring (multi-model)
- [ ] Set confidence thresholds (>90% = auto-accept, <70% = review)
- **Estimate:** 2 hours

---

### Epic 4: Spec Extraction & Parsing

**TASK-013: Extract Pipe Specifications**
- [ ] Parse pipe size (diameter in inches or DN)
- [ ] Extract pipe schedule (Sch 40, Sch 80, etc.)
- [ ] Identify material type (carbon steel, stainless, PVC)
- [ ] Capture line numbers (e.g., "CW-101")
- [ ] Extract service descriptions (e.g., "cooling water")
- **Estimate:** 3 hours

**TASK-014: Extract Fitting Specifications**
- [ ] Identify fitting types (elbows, tees, reducers, unions)
- [ ] Capture fitting angles (90°, 45°, etc.)
- [ ] Extract fitting sizes
- [ ] Count quantities per drawing
- [ ] Detect weldolets, sockolets, threadolets
- **Estimate:** 3 hours

**TASK-015: Extract Valve & Component Specs**
- [ ] Identify valve types (gate, ball, globe, check, butterfly)
- [ ] Capture valve sizes and materials
- [ ] Detect flanges (slip-on, weld-neck, blind)
- [ ] Extract actuator types (manual, electric, pneumatic)
- **Estimate:** 2 hours

**TASK-016: Validate Extracted Specs**
- [ ] Check pipe sizes against ASME/ANSI standards
- [ ] Validate material codes (A106, A312, etc.)
- [ ] Verify fitting sizes match pipe sizes
- [ ] Flag invalid/unknown specifications
- **Estimate:** 2 hours

---

### Epic 5: Measurement Engine

**TASK-017: Detect Drawing Scale**
- [ ] Extract scale from text annotations (e.g., "1:50", "1/4\"=1'")
- [ ] Handle metric and imperial scales
- [ ] Parse scale from title blocks
- [ ] Default to common scales if not found (flag for review)
- **Estimate:** 2 hours

**TASK-018: Measure Pipe Lengths**
- [ ] Trace pipe runs in drawing (pixel coordinates)
- [ ] Calculate pixel length along pipe path
- [ ] Convert pixels to real-world units using scale
- [ ] Handle diagonal and curved pipe runs
- [ ] Sum total length per line number
- **Estimate:** 4 hours

**TASK-019: Calculate Fitting Allowances**
- [ ] Add weld gap allowances for butt-weld fittings
- [ ] Calculate flange bolt lengths
- [ ] Add thread engagement lengths
- [ ] Apply standard fitting dimensions (ASME B16.9)
- **Estimate:** 2 hours

**TASK-020: Calculate Support Spacing**
- [ ] Apply pipe support spacing rules (per ASME B31.3)
- [ ] Calculate number of supports based on pipe length
- [ ] Account for material-specific spacing (steel vs plastic)
- [ ] Include support types (clamp, hanger, shoe)
- **Estimate:** 2 hours

---

### Epic 6: Bill of Materials Generation

**TASK-021: Design BOM Data Structure**
- [ ] Define BOM schema (item, description, size, qty, material)
- [ ] Create Pydantic model for BOM
- [ ] Support grouped items (e.g., all 2" elbows together)
- [ ] Include metadata (project, date, engineer, confidence)
- **Estimate:** 1 hour

**TASK-022: Generate BOM from Extracted Specs**
- [ ] Aggregate specs across all drawings
- [ ] Group similar items (same size + type + material)
- [ ] Calculate total quantities
- [ ] Sort BOM by line number or item type
- [ ] Add item numbers (sequential)
- **Estimate:** 3 hours

**TASK-023: Implement BOM Review/Editing**
- [ ] Allow user to manually edit quantities
- [ ] Enable adding custom items (not in drawings)
- [ ] Support deleting incorrect extractions
- [ ] Track edits with change log
- **Estimate:** 3 hours

**TASK-024: Add BOM Validation Rules**
- [ ] Check for missing required fields
- [ ] Validate quantities (positive numbers only)
- [ ] Flag unusual combinations (e.g., 12" valve on 2" pipe)
- [ ] Warn about low-confidence items
- **Estimate:** 2 hours

---

### Epic 7: Export Functionality

**TASK-025: Implement Excel Export**
- [ ] Install openpyxl or xlsxwriter library
- [ ] Create Excel template with headers
- [ ] Populate BOM data into spreadsheet
- [ ] Format cells (bold headers, number formatting)
- [ ] Add metadata sheet (project info, confidence scores)
- **Estimate:** 3 hours

**TASK-026: Implement CSV Export**
- [ ] Create CSV export function
- [ ] Include all BOM columns
- [ ] Handle special characters (commas in descriptions)
- [ ] Add UTF-8 BOM for Excel compatibility
- **Estimate:** 1 hour

**TASK-027: Implement PDF Export (Optional)**
- [ ] Use ReportLab or WeasyPrint
- [ ] Create PDF template matching Excel format
- [ ] Include project header and footer
- [ ] Add page numbers
- **Estimate:** 3 hours

---

### Epic 8: Testing & Validation

**TASK-028: Create Test Drawing Samples**
- [ ] Collect 5-10 sample piping drawings (various types)
- [ ] Get drawings from your friend (real-world examples)
- [ ] Create synthetic test drawings (simple cases)
- [ ] Include edge cases (poor scans, complex layouts)
- **Estimate:** 2 hours

**TASK-029: Build Unit Tests**
- [ ] Test PDF parsing functions
- [ ] Test spec extraction logic
- [ ] Test BOM generation
- [ ] Test export functions
- [ ] Aim for 80%+ code coverage
- **Estimate:** 4 hours

**TASK-030: Build Integration Tests**
- [ ] Test full PDF → BOM workflow
- [ ] Test multi-page PDF processing
- [ ] Test error handling (corrupt PDFs, API failures)
- [ ] Test export formats (Excel, CSV)
- **Estimate:** 3 hours

**TASK-031: Manual QA with Real Drawings**
- [ ] Run tool on your friend's actual drawings
- [ ] Compare AI-generated BOM vs manual BOM
- [ ] Measure accuracy (% items correctly extracted)
- [ ] Identify failure modes (what AI misses)
- [ ] Document improvements needed
- **Estimate:** 4 hours

**TASK-032: Performance Testing**
- [ ] Test with 100-page PDF
- [ ] Measure processing time per page
- [ ] Optimize slow operations (image processing, API calls)
- [ ] Set up monitoring/logging for production
- **Estimate:** 2 hours

---

### Epic 9: User Interface (Simple MVP)

**TASK-033: Build Streamlit Prototype**
- [ ] Create Streamlit app for PDF upload
- [ ] Show upload progress bar
- [ ] Display extracted specs in table
- [ ] Add BOM review/edit UI
- [ ] Add export buttons (Excel, CSV)
- **Estimate:** 4 hours

**TASK-034: Add Confidence Score Visualization**
- [ ] Show confidence scores next to each item
- [ ] Highlight low-confidence items in red/yellow
- [ ] Allow user to mark items as "reviewed"
- [ ] Show overall BOM confidence score
- **Estimate:** 2 hours

**TASK-035: Add Drawing Preview**
- [ ] Display drawing images in UI
- [ ] Highlight detected pipes/fittings on image
- [ ] Allow zoom/pan for detailed review
- [ ] Show which items came from which page
- **Estimate:** 3 hours

---

## Phase 2: Cost Estimation (Post-MVP)

**TASK-036: Build Pricing Database**
- [ ] Create pricing table (item, unit cost, labor rate)
- [ ] Import pricing data (CSV or API integration)
- [ ] Support multiple vendors (McMaster-Carr, Ferguson)
- [ ] Allow user to override prices
- **Estimate:** 4 hours

**TASK-037: Implement Cost Calculation Engine**
- [ ] Calculate material cost (qty × unit price)
- [ ] Calculate labor cost (installation time × rate)
- [ ] Apply markup/margin (configurable %)
- [ ] Generate cost breakdown by category
- **Estimate:** 3 hours

**TASK-038: Generate Customer Proposal**
- [ ] Create proposal template (PDF/Word)
- [ ] Include project scope and specs
- [ ] Add cost summary and payment terms
- [ ] Export to branded PDF
- **Estimate:** 3 hours

---

## Phase 3: Production Deployment

**TASK-039: Dockerize Application**
- [ ] Create Dockerfile for backend
- [ ] Create Dockerfile for frontend (if React)
- [ ] Update docker-compose.yml for production
- [ ] Set up environment variable management
- **Estimate:** 2 hours

**TASK-040: Deploy to Cloud**
- [ ] Choose hosting provider (Railway, Render, Fly.io)
- [ ] Deploy backend API
- [ ] Deploy frontend (if separate)
- [ ] Set up PostgreSQL database
- [ ] Configure environment variables
- **Estimate:** 3 hours

**TASK-041: Set Up Monitoring & Logging**
- [ ] Add application logging (Python logging module)
- [ ] Set up error tracking (Sentry or similar)
- [ ] Monitor API usage and costs
- [ ] Create health check dashboard
- **Estimate:** 2 hours

**TASK-042: Write User Documentation**
- [ ] Create user guide (how to upload PDFs)
- [ ] Document BOM review workflow
- [ ] Add troubleshooting section
- [ ] Create video walkthrough
- **Estimate:** 3 hours

**TASK-043: User Training & Onboarding**
- [ ] Walk your friend through the tool
- [ ] Get feedback on usability
- [ ] Identify missing features
- [ ] Iterate based on feedback
- **Estimate:** 2 hours

---

## Task Summary

**Phase 1 (MVP):** 43 tasks, ~100 hours (2-3 weeks full-time)

**Quick Wins (Start Here):**
1. TASK-001: Project setup (1h)
2. TASK-002: AI API setup (2h)
3. TASK-005: PDF upload endpoint (2h)
4. TASK-009: Vision prompts (3h)
5. TASK-010: Claude integration (4h)
6. TASK-013: Pipe spec extraction (3h)
7. TASK-022: BOM generation (3h)
8. TASK-025: Excel export (3h)

**Critical Path:**
```
Setup → PDF Upload → AI Vision → Spec Extraction → BOM Generation → Export → Testing
```

---

## Open Questions (Need Answers Before Starting)

1. **Sample Drawings:** Can your friend provide 3-5 real PDF drawings for testing?
2. **Drawing Standards:** What standards does he typically work with? (ASME, ISO, DIN?)
3. **Typical Project Size:** How many pages per typical project? (10? 100? 500?)
4. **Existing Tools:** What software does he currently use for estimates? (Excel? QuickBooks? Custom software?)
5. **Pricing Data:** Does he have a materials pricing database we can import?
6. **Success Criteria:** What accuracy % would make him trust the tool? (90%? 95%? 99%?)

---

## Next Steps

1. ✅ PRD written
2. ✅ Task list created
3. ⏳ Get sample drawings from your friend
4. ⏳ Start with TASK-001 (project setup)
5. ⏳ Build proof-of-concept (single drawing → BOM)
6. ⏳ Demo to your friend and get feedback
7. ⏳ Iterate based on real-world usage

---

**Ready to start coding!** 🚀

Let me know when you have sample drawings, and we can begin with the quick wins.
