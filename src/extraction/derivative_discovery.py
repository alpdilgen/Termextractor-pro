"""
Derivative Discovery for TermExtractor-Pro
Finds morphological variants (prefix/suffix additions) of single-word terms
Logic adapted from TermCorrector's derived_term_finder
"""

import re
from typing import List, Dict, Optional, Set
from src.utils import is_single_word, DERIVATIVE_WORD_CHARS


class DerivativeDiscovery:
    """Find morphological derivatives of single-word terms"""
    
    def __init__(
        self,
        enabled: bool = False,
        modes: Optional[List[str]] = None,
        min_variant_length: int = 3,
        max_variants_per_term: int = 20,
        case_sensitive: bool = False,
    ):
        """
        Initialize derivative discovery.
        
        Args:
            enabled: Whether discovery is enabled
            modes: Search modes ['prefix', 'suffix', 'any']
            min_variant_length: Minimum length for variant
            max_variants_per_term: Maximum variants to return per term
            case_sensitive: Whether matching is case-sensitive
        """
        self.enabled = enabled
        self.modes = modes or ['prefix', 'suffix']
        self.min_variant_length = min_variant_length
        self.max_variants_per_term = max_variants_per_term
        self.case_sensitive = case_sensitive
        
        # Word character pattern (Unicode-aware)
        self.WORD_CHARS = DERIVATIVE_WORD_CHARS
        
        # Statistics
        self.statistics = {
            'terms_processed': 0,
            'single_word_terms': 0,
            'derivatives_found': 0,
            'avg_derivatives_per_term': 0.0,
        }
    
    def find_derivatives(self, term: str, text: str) -> List[str]:
        """
        Find derivative variants of a term in text.
        
        Args:
            term: Base term to search for
            text: Full text to search in
            
        Returns:
            List of unique derivatives found
        """
        if not self.enabled or not is_single_word(term):
            return []
        
        if not text or not term:
            return []
        
        # Escape term for regex
        term_escaped = re.escape(term)
        patterns: List[re.Pattern] = []
        
        # Build regex patterns based on modes
        flags = 0 if self.case_sensitive else (re.IGNORECASE | re.UNICODE)
        
        # PREFIX mode: base + suffix
        # Example: "machine" -> "machines", "machinery", "machinist"
        if 'prefix' in self.modes:
            patterns.append(
                re.compile(
                    rf"\b{term_escaped}{self.WORD_CHARS}+",
                    flags
                )
            )
        
        # SUFFIX mode: prefix + base
        # Example: "machine" -> "unmachine", "machineable"
        if 'suffix' in self.modes:
            patterns.append(
                re.compile(
                    rf"{self.WORD_CHARS}+{term_escaped}\b",
                    flags
                )
            )
        
        # ANY mode: aggressive matching
        # Example: "machine" -> anywhere in compound
        if 'any' in self.modes:
            patterns.append(
                re.compile(
                    rf"{self.WORD_CHARS}*{term_escaped}{self.WORD_CHARS}*",
                    flags
                )
            )
        
        # Find all matches
        derivatives: Set[str] = set()
        
        for pattern in patterns:
            for match in pattern.finditer(text):
                word = match.group(0).strip()
                
                if not word:
                    continue
                
                # Skip if too short
                if len(word) < self.min_variant_length:
                    continue
                
                # Skip if it's the base term itself
                if self.case_sensitive:
                    if word == term:
                        continue
                else:
                    if word.lower() == term.lower():
                        continue
                
                derivatives.add(word)
        
        # Sort and limit
        result = sorted(list(derivatives), key=lambda x: x.lower())
        return result[:self.max_variants_per_term]
    
    def enrich_term(self, term_dict: Dict, full_text: str) -> Dict:
        """
        Enrich a term with discovered derivatives.
        
        Args:
            term_dict: Term dictionary (with 'term' key)
            full_text: Full extraction text
            
        Returns:
            Enriched term dictionary
        """
        if not self.enabled:
            return term_dict
        
        term_text = term_dict.get('term', '')
        
        if not term_text or not is_single_word(term_text):
            return term_dict
        
        self.statistics['terms_processed'] += 1
        self.statistics['single_word_terms'] += 1
        
        # Find derivatives
        derivatives = self.find_derivatives(term_text, full_text)
        
        if derivatives:
            self.statistics['derivatives_found'] += len(derivatives)
            
            # Add to variants if they exist
            existing_variants = term_dict.get('variants', [])
            if existing_variants and isinstance(existing_variants, list):
                all_variants = list(set(existing_variants + derivatives))
            else:
                all_variants = derivatives
            
            term_dict['variants'] = sorted(all_variants)
            
            # Store discovered derivatives in metadata
            if 'metadata' not in term_dict:
                term_dict['metadata'] = {}
            
            term_dict['metadata']['discovered_derivatives'] = derivatives
            term_dict['metadata']['derivative_discovery_enabled'] = True
        
        return term_dict
    
    def get_statistics(self) -> Dict[str, any]:
        """Get discovery statistics"""
        stats = self.statistics.copy()
        
        if stats['single_word_terms'] > 0:
            stats['avg_derivatives_per_term'] = (
                stats['derivatives_found'] / stats['single_word_terms']
            )
        
        return stats
    
    def reset_statistics(self) -> None:
        """Reset statistics"""
        self.statistics = {
            'terms_processed': 0,
            'single_word_terms': 0,
            'derivatives_found': 0,
            'avg_derivatives_per_term': 0.0,
        }


class DerivativeConfig:
    """Configuration for derivative discovery"""
    
    def __init__(
        self,
        enabled: bool = False,
        modes: Optional[List[str]] = None,
        min_variant_length: int = 3,
        max_variants_per_term: int = 20,
        case_sensitive: bool = False,
    ):
        """Initialize configuration"""
        self.enabled = enabled
        self.modes = modes or ['prefix', 'suffix']
        self.min_variant_length = min_variant_length
        self.max_variants_per_term = max_variants_per_term
        self.case_sensitive = case_sensitive
