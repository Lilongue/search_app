from base64 import b64decode
import requests
from xml_parser import XmlParser


class YaSearchRequestData:
    """
    Класс для хранения данных для запроса к Яндекс.Поиску
    """

    def __init__(self, query_text: str, folder_id: str, page_size: int = 10, ):
        self.query_text = query_text
        self.folder_id = folder_id
        self.page_size = page_size

    def to_dict(self):
        return {
            "query": {
                "search_type": "SEARCH_TYPE_RU",
                "queryText": self.query_text,
                "familyMode": "FAMILY_MODE_STRICT",
            },
            "groupSpec": {
                "groupsOnPage": self.page_size,
            },
            "folderID": self.folder_id,
            "responseFormat": "FORMAT_XML",
        }


class YaSearch:
    """
    Класс для выполнения запросов к Яндекс.Поиску
    """

    def __init__(self, api_key: str):
        self.api_key = api_key

    def search(self, query_text: str, folder_id: str, page_size: int = 10, ):
        request_data = YaSearchRequestData(query_text, folder_id, page_size)
        if self.api_key is None:
            raise ValueError("api_key is required")
        response = requests.post(
            "https://searchapi.api.cloud.yandex.net/v2/web/search",
            headers={
                "Authorization": f"Api-Key {self.api_key}"
            },
            json=request_data.to_dict()
        )
        return XmlParser.parse_xml(b64decode(response.json().get("rawData", "")))
