# Piping Estimator 🔧

**AI-powered tool to automate piping estimation from PDF drawings**

---

## Problem

Mechanical engineers spend **4+ hours per estimate** manually:
- Reading hundreds of pages of PDF drawings
- Extracting pipe specs (sizes, materials, lengths, fittings)
- Calculating quantities
- Creating Bill of Materials (BOM)

## Solution

**Piping Estimator** uses AI vision models to:
- ✅ Analyze PDF drawings automatically
- ✅ Extract pipe specifications (size, schedule, material, length)
- ✅ Identify and count fittings, valves, and components
- ✅ Generate Bill of Materials (BOM) in minutes
- ✅ Export to Excel/CSV

**Time Savings:** 4 hours → 15 minutes ⚡

---

## Features (MVP)

- 📄 **PDF Upload:** Single or multi-page drawing packages
- 🤖 **AI Vision Analysis:** Claude Sonnet 4.5 / GPT-4V extract specs
- 📏 **Automatic Measurements:** Pipe lengths from scale drawings
- 🔩 **Fitting Detection:** Elbows, tees, valves, flanges, reducers
- 📊 **BOM Generation:** Itemized bill of materials with quantities
- 📥 **Export:** Excel, CSV, PDF formats
- ✅ **Confidence Scores:** Know which extractions to review

---

## Technology Stack

**Backend:**
- Python 3.11+
- FastAPI (REST API)
- LangChain (AI orchestration)
- Anthropic Claude API (vision)
- PyMuPDF (PDF processing)
- PostgreSQL (database)

**Frontend:**
- Streamlit (MVP prototype)
- React + TypeScript (future)

**Deployment:**
- Docker + docker-compose
- Railway / Render / Fly.io

---

## Quick Start

### Prerequisites

- Python 3.11+
- Docker & docker-compose
- Anthropic API key ([get one here](https://console.anthropic.com))
- OpenAI API key (optional, for GPT-4V fallback)

### Installation

```bash
# Clone the repository
git clone https://github.com/scott-fed/piping-estimator.git
cd piping-estimator

# Create virtual environment
python3.11 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env and add your API keys

# Start database
docker-compose up -d postgres

# Run database migrations
alembic upgrade head

# Start the API server
uvicorn src.main:app --reload
```

### Usage

```bash
# Start Streamlit UI
streamlit run src/app.py

# Or use the API directly
curl -X POST http://localhost:8000/api/upload \
  -F "file=@drawing.pdf"
```

---

## Project Structure

```
piping-estimator/
├── src/
│   ├── main.py              # FastAPI app
│   ├── api/                 # API endpoints
│   │   ├── upload.py        # PDF upload
│   │   ├── analyze.py       # AI vision analysis
│   │   └── export.py        # BOM export
│   ├── models/              # Database models
│   ├── services/            # Business logic
│   │   ├── pdf_processor.py
│   │   ├── vision_analyzer.py
│   │   ├── spec_extractor.py
│   │   └── bom_generator.py
│   ├── utils/               # Helper functions
│   └── app.py               # Streamlit UI
├── tests/                   # Unit & integration tests
├── docs/                    # Documentation
│   ├── PRD.md               # Product Requirements
│   └── TASKS.md             # Task breakdown
├── alembic/                 # Database migrations
├── docker-compose.yml       # Local development setup
├── requirements.txt         # Python dependencies
├── .env.example             # Environment variable template
└── README.md                # This file
```

---

## Roadmap

### Phase 1: MVP (2-3 weeks) ✅
- [x] PDF upload and processing
- [x] AI vision analysis
- [x] Spec extraction (pipes, fittings, valves)
- [x] BOM generation
- [x] Excel/CSV export

### Phase 2: Cost Estimation (1-2 weeks)
- [ ] Pricing database integration
- [ ] Cost calculation (materials + labor)
- [ ] Markup and margin
- [ ] Customer proposal generation

### Phase 3: Production (1 week)
- [ ] Docker deployment
- [ ] Cloud hosting (Railway/Render)
- [ ] Monitoring and logging
- [ ] User documentation

### Future Enhancements
- [ ] 3D model support (STEP, IFC files)
- [ ] P&ID diagram analysis
- [ ] Multi-user collaboration
- [ ] Mobile app
- [ ] ERP integration (Procore, Sage, QuickBooks)

---

## How It Works

### 1. Upload PDF Drawings
```python
# User uploads PDF drawing package
POST /api/upload
```

### 2. AI Vision Analysis
```python
# Claude Sonnet 4.5 analyzes each page
- Extract pipe specs (size, schedule, material)
- Measure pipe lengths from scale
- Identify fittings and valves
- Count quantities
```

### 3. Generate BOM
```python
# System aggregates specs and generates BOM
{
  "item": 1,
  "description": "Pipe, 4\" Sch 40 Carbon Steel",
  "quantity": "125.5 LF",
  "confidence": 0.95
}
```

### 4. Export
```python
# Download Excel, CSV, or PDF
GET /api/export?format=xlsx
```

---

## Accuracy & Validation

**Target Accuracy:** 95%+ on pipe spec extraction

**Validation Methods:**
- Multi-model cross-validation (Claude + GPT-4V)
- Confidence scoring (flag low-confidence items)
- Manual review UI (edit/correct extractions)
- Pipe standard validation (ASME/ANSI)

**Confidence Thresholds:**
- ✅ **>90%:** Auto-accept
- ⚠️ **70-90%:** Flag for review
- ❌ **<70%:** Manual verification required

---

## Contributing

This is a private project for a specific use case. If you want to contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## Testing

```bash
# Run unit tests
pytest tests/unit/

# Run integration tests
pytest tests/integration/

# Run with coverage
pytest --cov=src tests/

# Manual testing with sample drawings
python scripts/test_drawing.py sample_drawings/P-001.pdf
```

---

## Cost Estimation

**AI API Costs (Anthropic Claude):**
- ~$0.10-0.50 per drawing page (depending on complexity)
- 100-page drawing package: ~$10-50

**Optimization:**
- Use smaller models for page classification
- Only send relevant pages to expensive vision models
- Cache results to avoid re-processing

---

## Troubleshooting

### PDF Upload Fails
- Check file size (<100 MB)
- Verify file is a valid PDF
- Ensure storage directory has write permissions

### AI Vision Errors
- Verify API keys in `.env`
- Check API rate limits
- Review image quality (enhance contrast if needed)

### Low Accuracy
- Improve image preprocessing (denoise, enhance)
- Use multi-model validation
- Provide better prompt examples

### Slow Processing
- Optimize image resolution (don't send full-res images)
- Use concurrent API calls (batch processing)
- Cache intermediate results

---

## FAQ

**Q: What drawing formats are supported?**  
A: Currently only PDF. Future: DWG, DXF, STEP, IFC.

**Q: How accurate is the AI extraction?**  
A: Target is 95%+. Accuracy depends on drawing quality and clarity.

**Q: Can I edit the BOM before exporting?**  
A: Yes! Manual review/editing is built into the UI.

**Q: What pipe standards are supported?**  
A: ASME/ANSI (NPS). ISO/DIN support coming soon.

**Q: Does it work with scanned drawings?**  
A: Yes, but quality matters. OCR + image enhancement help.

**Q: Can it handle 3D models?**  
A: Not yet. Phase 3 will add STEP/IFC support.

---

## License

MIT License - See [LICENSE](LICENSE) file for details.

---

## Contact

**Project Lead:** Scott Federoff  
**AI Assistant:** Shelby (OpenClaw)  
**GitHub:** [scott-fed/piping-estimator](https://github.com/scott-fed/piping-estimator)

---

## Acknowledgments

- Anthropic (Claude AI)
- OpenAI (GPT-4V)
- Open-source community

---

**Built with ❤️ to help mechanical engineers save time and focus on what matters.**
