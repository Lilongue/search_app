import xml.etree.ElementTree as ET
from typing import List


class XmlParser:
    @classmethod
    def parse_xml(cls, xml_data: str) -> List[str]:
        urls = []
        if not xml_data:
            return urls
        root = ET.fromstring(xml_data)
        for url_element in root.findall('.//url'):
            if url_element.text:
                urls.append(url_element.text)
        return urls
