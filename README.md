# TermExtractor-Pro 🔍

**AI-powered terminology extraction with bilingual lookup and morphological variant discovery**

Extract key terms and concepts from documents using Claude AI, automatically find existing translations in bilingual files, and discover morphological variants of single-word terms.

---

## ✨ Features

### 🤖 AI-Powered Extraction
- Uses Claude 3.5 (Haiku for speed, Sonnet for complex analysis)
- Cost-optimized model selection
- Intelligent domain classification
- Multi-level domain hierarchy support

### 🌐 Bilingual Lookup
- Exact matching with existing translations
- Fuzzy matching with configurable threshold
- Supports XLIFF, SDLXLIFF, MQXLIFF formats
- Automatic language detection
- Reduces API calls by reusing translations

### 🔬 Derivative Discovery
- Finds morphological variants (prefix/suffix additions)
- Configurable search patterns (prefix, suffix, any)
- Perfect for building comprehensive terminology databases
- Supports Unicode and special characters

### 📊 Multiple Export Formats
- **XLSX**: Spreadsheet with sheets for terms, derivatives, and statistics
- **CSV**: Standard comma-separated values
- **JSON**: Structured data for APIs and automation
- **TBX**: Terminology Exchange format for CAT tools

### 📈 Rich Statistics
- Relevance scoring (0-100)
- Confidence assessment
- Frequency counting
- Domain hierarchy tracking
- Bilingual lookup metrics
- Derivative discovery statistics

### 🎯 Advanced Configuration
- Customizable relevance thresholds
- Domain-specific extraction hints
- Multi-language support (20+)
- Batch processing ready
- Comprehensive logging

---

## 🚀 Quick Start

### 1. Installation

```bash
git clone https://github.com/yourusername/TermExtractor-Pro.git
cd TermExtractor-Pro
pip install -r requirements.txt
```

### 2. Get API Key

1. Visit https://console.anthropic.com
2. Create a new API key
3. Copy the key

### 3. Run Application

```bash
streamlit run streamlit_app.py
```

### 4. Configure and Extract

1. Paste your API key in the sidebar
2. Go to **Extract** tab
3. Upload a document (PDF, DOCX, TXT, etc.)
4. Configure language pair and optional domain
5. Enable bilingual lookup and/or derivative discovery (optional)
6. Click **Extract Terms**
7. Review results in **Results** tab
8. Export in your preferred format

---

## 📖 Usage Guide

### Basic Extraction

```python
from src.extraction import TermExtractor

extractor = TermExtractor(api_key="your-api-key")

result = extractor.extract(
    file_path="document.pdf",
    source_lang="en",
    target_lang="de",
    domain_path="Medical/Healthcare"
)

# Export results
xlsx_data = extractor.export_result(result, "xlsx")
```

### With Bilingual Lookup

```python
result = extractor.extract(
    file_path="document.pdf",
    source_lang="en",
    target_lang="de",
    enable_bilingual_lookup=True,
    bilingual_file_path="existing_translations.xliff",
    fuzzy_threshold=70
)
```

### With Derivative Discovery

```python
result = extractor.extract(
    file_path="document.pdf",
    source_lang="en",
    enable_derivative_discovery=True,
    derivative_modes=["prefix", "suffix"]
)
```

### Accessing Results

```python
# Get high-relevance terms
high_relevance = result.get_high_relevance_terms(threshold=80)

# Access statistics
print(result.statistics)
print(result.lookup_statistics)
print(result.derivative_statistics)

# Iterate through terms
for term in result.terms:
    print(f"{term.term} → {term.translation}")
    print(f"  Domain: {term.domain}")
    print(f"  Relevance: {term.relevance_score}")
    print(f"  Derivatives: {term.discovered_derivatives}")
```

---

## 🗂️ Project Structure

```
TermExtractor-Pro/
├── streamlit_app.py              # Main Streamlit application
├── pages/
│   ├── extraction.py             # Term extraction page
│   ├── results.py                # Results display page
│   └── settings.py               # Settings and configuration
├── src/
│   ├── __init__.py
│   ├── config/
│   │   ├── config.py             # Configuration manager
│   │   └── config.yaml           # Configuration settings
│   ├── models/
│   │   └── data_models.py        # Data classes (Term, ExtractionResult)
│   ├── extraction/
│   │   ├── term_extractor.py     # Main extraction orchestrator
│   │   ├── bilingual_file_handler.py
│   │   ├── translation_lookup.py
│   │   └── derivative_discovery.py
│   ├── api/
│   │   ├── anthropic_client.py   # Anthropic API client
│   │   └── api_manager.py        # API orchestration & caching
│   ├── io/
│   │   ├── file_parser.py        # Multi-format file parsing
│   │   └── format_exporter.py    # Multi-format export
│   └── utils/
│       ├── constants.py          # Application constants
│       └── helpers.py            # Utility functions
├── requirements.txt
└── README.md
```

---

## 🔧 Configuration

Edit `src/config/config.yaml` to customize:

```yaml
extraction:
  default_relevance_threshold: 70.0    # Default term quality threshold
  chunk_size: 2000                     # Characters per processing chunk

model_selection:
  extraction_model: "claude-3-5-haiku-20241022"  # Fast, cheap
  domain_classification_model: "claude-3-5-haiku-20241022"
  fuzzy_refinement_model: "claude-3-5-sonnet-20241022"  # Better reasoning

translation_lookup:
  enabled: false
  fuzzy_threshold: 70.0                # Minimum similarity for fuzzy match
  supported_formats: [xliff, sdlxliff, mqxliff]

derivative_discovery:
  enabled: false
  modes: [prefix, suffix]              # Search patterns
  max_variants_per_term: 20
```

---

## 🎯 Supported Languages

English, German, French, Spanish, Italian, Portuguese, Bulgarian, Romanian, Turkish, Russian, Japanese, Chinese, Arabic, Hindi, and more (30+ languages).

---

## 📊 Export Examples

### XLSX Export Structure
```
Sheet 1: Terms
- Full term details with all fields
- Color-coded by relevance (green: 80+, yellow: 60-79, pink: <60)

Sheet 2: Derivatives (if found)
- Base term | Derivative Count | Variants

Sheet 3: Statistics
- Extraction statistics
- Bilingual lookup metrics
- Derivative discovery stats
```

### JSON Export Structure
```json
{
  "metadata": {
    "source_language": "en",
    "target_language": "de",
    "domain_hierarchy": ["Medical", "Healthcare"]
  },
  "terms": [...],
  "statistics": {...},
  "lookup_statistics": {...},
  "derivative_statistics": {...}
}
```

---

## 💰 Cost Optimization

TermExtractor-Pro is designed for cost efficiency:

- **Model Selection**: Uses Haiku (4x cheaper than Sonnet) for simple extraction, Sonnet only for complex analysis
- **Caching**: Results cached to avoid redundant API calls
- **Bilingual Lookup**: Reduces API calls by reusing existing translations
- **Token Optimization**: Efficient prompts that minimize token usage

**Estimated Costs:**
- Small document (1000 words): ~$0.01
- Medium document (5000 words): ~$0.05
- Large document (20,000 words): ~$0.20

---

## 🔒 Security & Privacy

- API keys are never logged or stored
- All data is sent securely to Anthropic servers
- No data retention on TermExtractor-Pro servers
- GDPR and privacy-aware design
- Encryption for sensitive data in transit

---

## 🚀 Deployment

### Deploy to Streamlit Cloud

1. Push to GitHub
2. Visit https://share.streamlit.io
3. Connect your repository
4. Set `ANTHROPIC_API_KEY` secret in Streamlit dashboard
5. Deploy!

### Deploy to Other Platforms

Works with any Python hosting that supports Streamlit:
- Heroku
- Railway
- PythonAnywhere
- AWS / Azure / GCP
- Docker containers

---

## 📝 Supported Input Formats

- **Documents**: PDF, DOCX, TXT, HTML
- **Bilingual Files**: XLIFF, SDLXLIFF, MQXLIFF, XML
- **Max Size**: 100 MB
- **Languages**: Auto-detect or manual selection

---

## 🤝 Advanced Features

### For Professional Users

- **Termbase Integration**: Import and match against existing termbases
- **Quality Metrics**: Precision, recall, F1 scores
- **Batch Processing**: Process multiple documents efficiently
- **API Mode**: Use as FastAPI backend (coming soon)
- **Custom Prompts**: Fine-tune extraction behavior

### For Developers

- Modular architecture for easy customization
- Cost-optimized API client
- Rate limiting and caching built-in
- Comprehensive logging
- RESTful API ready

---

## 📊 Statistics & Metrics

Each extraction provides:

- **Relevance Score** (0-100): How important is the term to the text?
- **Confidence Score** (0-100): How confident is the AI in this extraction?
- **Frequency**: How many times does the term appear?
- **Domain Hierarchy**: Multi-level domain classification
- **Translation Source**: Where did the translation come from? (API, Exact, Fuzzy)
- **Fuzzy Match Score**: Similarity % for fuzzy matches
- **Discovered Variants**: Morphological forms of the term

---

## 🐛 Troubleshooting

### "API Key not found"
- Ensure you've set `ANTHROPIC_API_KEY` environment variable
- Or enter the key in the Streamlit sidebar

### "File parsing error"
- Ensure file is not corrupted
- Try exporting to another format and re-uploading
- Check file size (max 100 MB)

### "No terms extracted"
- Increase relevance threshold to show more terms
- Check if domain hint is too restrictive
- Verify source language is correct

### "Fuzzy matching not working"
- Increase fuzzy threshold (currently at what value?)
- Enable bilingual file upload
- Check file format is XLIFF/SDLXLIFF/MQXLIFF

---

## 📚 Documentation

- **User Guide**: See Settings tab in app
- **API Documentation**: Full docstrings in source code
- **Configuration**: Edit `src/config/config.yaml`
- **Examples**: See usage section above

---

## 🎓 Learning Resources

- [Anthropic Documentation](https://docs.anthropic.com)
- [Claude Models](https://www.anthropic.com/product)
- [Terminology Extraction Best Practices](https://en.wikipedia.org/wiki/Terminology_extraction)
- [XLIFF Standard](https://www.oasis-open.org/committees/tc_home.php?wg_abbrev=xliff)

---

## 📄 License

This project is open source and available under the MIT License.

---

## 🙋 Support

- **Issues**: Report bugs on GitHub
- **Discussions**: Ask questions in GitHub discussions
- **Email**: support@example.com

---

## 🎉 Acknowledgments

Built with:
- [Anthropic Claude API](https://www.anthropic.com)
- [Streamlit](https://streamlit.io)
- [Python](https://www.python.org)

---

**Happy Terminology Extraction! 🚀**

Made with ❤️ for translators, terminologists, and localization professionals worldwide.
