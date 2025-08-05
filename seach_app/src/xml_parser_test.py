import unittest
from xml_parser import XmlParser


class TestXmlParser(unittest.TestCase):

    def test_parse_xml_with_urls(self):
        xml_data = '''<?xml version="1.0" encoding="utf-8"?>
<yandexsearch version="1.0">
    <response>
        <results>
            <grouping>
                <group>
                    <doc>
                        <url>https://nastroenie-dental.ru/</url>
                    </doc>
                </group>
                <group>
                    <doc>
                        <url>https://yandex.ru/maps/org/nastroyeniye/1236750269/</url>
                    </doc>
                </group>
                <group>
                    <doc>
                        <url>https://zoon.ru/spb/medical/stomatologicheskaya_klinika_nastroenie_na_moskovskom_prospekte/</url>
                    </doc>
                </group>
            </grouping>
        </results>
    </response>
</yandexsearch>'''
        expected_urls = [
            "https://nastroenie-dental.ru/",
            "https://yandex.ru/maps/org/nastroyeniye/1236750269/",
            "https://zoon.ru/spb/medical/stomatologicheskaya_klinika_nastroenie_na_moskovskom_prospekte/"
        ]
        self.assertEqual(XmlParser.parse_xml(xml_data), expected_urls)

    def test_parse_xml_no_urls(self):
        xml_data = '''<?xml version="1.0" encoding="utf-8"?>
<yandexsearch version="1.0">
    <response>
        <results>
            <grouping>
                <group>
                    <doc>
                        <title>No url here</title>
                    </doc>
                </group>
            </grouping>
        </results>
    </response>
</yandexsearch> '''
        self.assertEqual(XmlParser.parse_xml(xml_data), [])

    def test_parse_xml_empty_input(self):
        self.assertEqual(XmlParser.parse_xml(""), [])


if __name__ == '__main__':
    unittest.main()
