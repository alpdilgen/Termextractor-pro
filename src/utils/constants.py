"""
Constants for TermExtractor-Pro
"""

# Claude Models (ordered by cost-efficiency for our use case)
CLAUDE_MODELS = {
    "extraction": "claude-3-5-haiku-20241022",  # Fast, cheap for simple text extraction
    "complex_analysis": "claude-3-5-sonnet-20241022",  # Better for fuzzy reference refinement
    "domain_classification": "claude-3-5-haiku-20241022",  # Fast domain detection
}

# Default model (fallback)
DEFAULT_MODEL = "claude-3-5-sonnet-20241022"

# Text processing
TEXT_CHUNK_SIZE = 2000  # Characters per chunk for large files
MIN_TERM_LENGTH = 2
MAX_TERM_LENGTH = 255

# Extraction defaults
DEFAULT_RELEVANCE_THRESHOLD = 70.0
DEFAULT_CONFIDENCE_THRESHOLD = 60.0

# Fuzzy matching
DEFAULT_FUZZY_THRESHOLD = 70.0
FUZZY_MATCH_MIN_SCORE = 50.0

# Derivative discovery
DERIVATIVE_WORD_CHARS = r"[A-Za-zÀ-ÖØ-öø-ÿßÜüÄäÖö0-9_]"
DEFAULT_DERIVATIVE_MODES = ["prefix", "suffix"]
DEFAULT_MAX_VARIANTS = 20
DEFAULT_MIN_VARIANT_LENGTH = 3

# Supported languages
SUPPORTED_LANGUAGES = {
    'af': 'Afrikaans',
    'sq': 'Albanian',
    'ar': 'Arabic',
    'hy': 'Armenian',
    'az': 'Azerbaijani',
    'eu': 'Basque',
    'be': 'Belarusian',
    'bn': 'Bengali',
    'bs': 'Bosnian',
    'bg': 'Bulgarian',
    'ca': 'Catalan',
    'zh': 'Chinese',
    'hr': 'Croatian',
    'cs': 'Czech',
    'da': 'Danish',
    'nl': 'Dutch',
    'en': 'English',
    'et': 'Estonian',
    'fi': 'Finnish',
    'fr': 'French',
    'gl': 'Galician',
    'ka': 'Georgian',
    'de': 'German',
    'el': 'Greek',
    'gu': 'Gujarati',
    'he': 'Hebrew',
    'hi': 'Hindi',
    'hu': 'Hungarian',
    'is': 'Icelandic',
    'id': 'Indonesian',
    'ga': 'Irish',
    'it': 'Italian',
    'ja': 'Japanese',
    'kn': 'Kannada',
    'kk': 'Kazakh',
    'ko': 'Korean',
    'lv': 'Latvian',
    'lt': 'Lithuanian',
    'mk': 'Macedonian',
    'ms': 'Malay',
    'ml': 'Malayalam',
    'mt': 'Maltese',
    'no': 'Norwegian',
    'ps': 'Pashto',
    'fa': 'Persian',
    'pl': 'Polish',
    'pt': 'Portuguese',
    'ro': 'Romanian',
    'ru': 'Russian',
    'sr': 'Serbian',
    'sk': 'Slovak',
    'sl': 'Slovenian',
    'es': 'Spanish',
    'sv': 'Swedish',
    'ta': 'Tamil',
    'te': 'Telugu',
    'th': 'Thai',
    'tr': 'Turkish',
    'uk': 'Ukrainian',
    'ur': 'Urdu',
    'vi': 'Vietnamese',
    'cy': 'Welsh',
    'yi': 'Yiddish',
}

# File formats
SUPPORTED_FILE_FORMATS = {
    'txt': 'Plain Text',
    'docx': 'Microsoft Word',
    'pdf': 'PDF',
    'html': 'HTML',
    'htm': 'HTML',
    'xliff': 'XLIFF',
    'sdlxliff': 'SDLXLIFF',
    'mqxliff': 'MQXLIFF',
    'xml': 'XML',
}

# Export formats
EXPORT_FORMATS = ['xlsx', 'csv', 'tbx', 'json']

# API rate limits
API_RATE_LIMIT_PER_MINUTE = 50
API_MAX_TOKENS_PER_REQUEST = 4096
API_TIMEOUT_SECONDS = 60

# Batch processing
BATCH_SIZE = 5
MAX_PARALLEL_REQUESTS = 3

# Statistics thresholds
HIGH_RELEVANCE_THRESHOLD = 80
MEDIUM_RELEVANCE_THRESHOLD = 60

# Export column names
EXPORT_COLUMNS = [
    'term',
    'translation',
    'from_existing_translation',
    'translation_source',
    'fuzzy_match_score',
    'discovered_derivatives',
    'domain',
    'subdomain',
    'pos',
    'definition',
    'context',
    'relevance_score',
    'confidence_score',
    'frequency',
    'is_compound',
    'is_abbreviation',
    'variants',
    'related_terms',
]

# Translation sources
TRANSLATION_SOURCE_API = "API"
TRANSLATION_SOURCE_EXACT = "EXACT_MATCH"
TRANSLATION_SOURCE_FUZZY = "FUZZY_REFERENCE"

# UI defaults
UI_THEME = "light"
UI_SIDEBAR_STATE = "expanded"
