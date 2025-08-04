import unittest
from siteInfoSearch import SiteInfoExtractor

class TestSiteInfoExtractor(unittest.TestCase):
    def setUp(self):
        self.extractor = SiteInfoExtractor()

    def test_normalize_phone(self):
        # Import InfoExtractor directly for testing normalize_phone
        from siteInfoSearch import InfoExtractor
        
        test_cases = [
            # input, expected output
            ("+7 (999) 123-45-67", "+79991234567"),
            ("8 (999) 123-45-67", "+79991234567"),
            ("+7-999-123-45-67", "+79991234567"),
            ("8-999-123-45-67", "+79991234567"),
            ("9991234567", "9991234567"),
            ("+79991234567", "+79991234567"),
            ("89991234567", "+79991234567"),
            (" 8 999 123 45 67 ", "+79991234567"),
            ("", ""),
            (None, None),
            ("+1 (234) 567-8900", "+12345678900"),
            ("123-456-7890", "1234567890"),
            ("+7‒921‒962‒15‒09", "+79219621509"),
            ("8 (921) 962-15-09", "+79219621509"),
        ]
        
        info_extractor = InfoExtractor("")
        for input_phone, expected in test_cases:
            with self.subTest(input_phone=input_phone):
                self.assertEqual(info_extractor.normalize_phone(input_phone), expected)

    def test_extract_phone_variously(self):
        # Test cases with different content scenarios
        test_cases = [
            # (processed_content, search_phone, expected_result)
            ("Contact us at +7 (999) 123-45-67", "+79991234567", "+7 (999) 123-45-67"),
            ("Call 8 (999) 123-45-67 for support", "89991234567", "8 (999) 123-45-67"),
            ("Phone: +7-999-123-45-67", "+79991234567", "+7-999-123-45-67"),
            ("Contact: 8-999-123-45-67", "89991234567", "8-999-123-45-67"),
            ("Our number is 999-123-45-67", "9991234567", "999-123-45-67"),
            ("Call +79991234567", "+79991234567", "+79991234567"),
            ("Phone 89991234567", "89991234567", "89991234567"),
            ("Contact: 8 999 123 45 67", "89991234567", "8 999 123 45 67"),
            ("No phone numbers here", "+79991234567", None),
            ("", "+79991234567", None),
            (None, "+79991234567", None),
            ("", "", ""),
            (None, None, None),
            ("Call +1 (234) 567-8900", "+12345678900", "+1 (234) 567-8900"),
            ("Phone: 123-456-7890", "1234567890", "123-456-7890"),
            ("Contact: +7-921-962-15-09", "+79219621509", "+7-921-962-15-09"),
            ("Call 8 (921) 962-15-09", "89219621509", "8 (921) 962-15-09"),
            # Multiple phones in content
            ("Call +7 (999) 123-45-67 or 8 (888) 456-78-90", "+79991234567", "+7 (999) 123-45-67"),
            ("Phone: 8 (999) 123-45-67, Fax: 8 (888) 456-78-90", "89991234567", "8 (999) 123-45-67"),
        ]
        
        for content, search_phone, expected in test_cases:
            with self.subTest(content=content, search_phone=search_phone):
                self.extractor._processed_content = content
                result = self.extractor._extract_phone_variously(search_phone)
                self.assertEqual(result, expected)

    def test_extract_phone_variously_edge_cases(self):
        # Test edge cases and boundary conditions
        test_cases = [
            # Empty or None inputs
            ("Some content", "", ""),
            ("Some content", None, None),
            ("", "+79991234567", None),
            (None, "+79991234567", None),
            
            # Phone numbers with different formatting but same normalized value
            ("Call +7 (999) 123-45-67", "8 (999) 123-45-67", "+7 (999) 123-45-67"),
            ("Phone: 8 (999) 123-45-67", "+7 (999) 123-45-67", "8 (999) 123-45-67"),
            
            # Phone numbers that don't match after normalization
            ("Call +7 (999) 123-45-67", "+7 (888) 123-45-67", None),
            ("Phone: 8 (999) 123-45-67", "8 (888) 123-45-67", None),
            
            # Content with multiple similar phone numbers
            ("Call +7 (999) 123-45-67 or +7 (999) 123-45-68", "+79991234567", "+7 (999) 123-45-67"),
            ("Phone: 8 (999) 123-45-67, Mobile: 8 (999) 123-45-68", "89991234567", "8 (999) 123-45-67"),
            
            # Test cases showing that various dash characters are now supported by regex
            ("Contact: +7‒921‒962‒15‒09", "+79219621509", "+7‒921‒962‒15‒09"),  # Figure dash (‒)
            ("Phone: +7–921–962–15–09", "+79219621509", "+7–921–962–15–09"),  # En dash (–)
            ("Call: +7—921—962—15—09", "+79219621509", "+7—921—962—15—09"),  # Em dash (—)
        ]
        
        for content, search_phone, expected in test_cases:
            with self.subTest(content=content, search_phone=search_phone):
                self.extractor._processed_content = content
                result = self.extractor._extract_phone_variously(search_phone)
                self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()