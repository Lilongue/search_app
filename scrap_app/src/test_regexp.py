#!/usr/bin/env python3
"""
Demonstration script showing the improved phone regex pattern
that now handles various dash characters.
"""

import re
from siteInfoSearch import InfoExtractor

def demo_regex_improvement():
    """Demonstrate the improved regex pattern for phone number extraction."""
    
    # Test text with various dash characters
    test_text = """
    Contact us at +7 (999) 123-45-67
    Call +7–921–962–15–09 for support
    Phone: +7—123—456—78—90
    Mobile: +7‒987‒654‒32‒10
    """
    
    print("Testing phone number extraction with various dash characters:")
    print("=" * 60)
    print(f"Test text:\n{test_text}")
    
    # Create InfoExtractor instance
    extractor = InfoExtractor(test_text)
    
    # Extract phones
    found_phones = extractor.extract_phones()
    
    print(f"\nFound phone numbers: {found_phones}")
    print(f"Total found: {len(found_phones)}")
    
    # Test normalization
    print("\nTesting normalization:")
    for phone in found_phones:
        normalized = extractor.normalize_phone(phone)
        print(f"  '{phone}' -> '{normalized}'")

if __name__ == "__main__":
    demo_regex_improvement()