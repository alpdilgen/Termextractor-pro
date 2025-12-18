"""TermExtractor-Pro - AI-powered terminology extraction system"""

from src.config import ConfigManager, config, get_config
from src.models import (
    Term,
    ExtractionResult,
    ExtractionConfig,
    BilinguialLookupStatistics,
    DerivativeStatistics,
)
from src.extraction import (
    TermExtractor,
    BilingualFileHandler,
    TranslationLookup,
    DerivativeDiscovery,
)
from src.api import AnthropicClient, APIManager
from src.io import FileParser, FormatExporter
from src.utils import (
    chunk_text,
    normalize_language_code,
    is_single_word,
    clean_text,
)

__version__ = "1.0.0"
__author__ = "TermExtractor-Pro"

__all__ = [
    # Core
    'TermExtractor',
    # API
    'AnthropicClient',
    'APIManager',
    # Models
    'Term',
    'ExtractionResult',
    'ExtractionConfig',
    # Features
    'BilingualFileHandler',
    'TranslationLookup',
    'DerivativeDiscovery',
    # I/O
    'FileParser',
    'FormatExporter',
    # Config
    'config',
    'get_config',
    'ConfigManager',
]
