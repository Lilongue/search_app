from flask import Flask, request, jsonify
from selenium_handler import SeleniumHandler
from employer_info import EmployerInfo
from siteInfoSearch import SiteInfoExtractor

app = Flask(__name__)
selenium_handler = SeleniumHandler()


@app.route('/parse', methods=['POST'])
def parse():
    """
    HTTP эндпоинт для обработки запросов на парсинг

    Ожидаемый JSON payload:
    {
        "url": "https://example.com",
        "phone": "+7 (999) 999-99-99",
        "email": "example@example.com",
        "site": "https://example.com",
        "organization_name": "ИП Иванов",
        "contact_person_name": "Иванов Иван",
        "code": ""
    }

    Returns:
        JSON ответ с содержимым или сообщением об ошибке
    """
    url = request.json.get('url')
    phone = request.json.get('phone')
    site = request.json.get('site')
    organization_name = request.json.get('organization_name')
    contact_person_name = request.json.get('contact_person_name')
    code = request.json.get('code')
    email = request.json.get('email')

    employer_info = EmployerInfo(phone, email, site, organization_name, contact_person_name, code)

    if not url:
        return jsonify({'error': 'URL required'}), 400

    try:
        site_info_extractor = SiteInfoExtractor()
        _ = site_info_extractor.get_site_info(url)
        extracted_info = site_info_extractor.extract_employer_info(employer_info)
        return jsonify({'employer_info': {
            'phone': extracted_info.phone,
            'email': extracted_info.email,
            'site': extracted_info.site,
            'organization_name': extracted_info.organization_name,
            'contact_person_name': extracted_info.contact_person_name,
            'inn_code': extracted_info.code
        }})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/text', methods=['POST'])
def scrape():
    """
    HTTP эндпоинт для получения текста с сайта

    Ожидаемый JSON payload:
    {
        "url": "https://example.com"
    }

    Returns:
        JSON ответ с текстом с сайта или сообщением об ошибке
    """
    url = request.json.get('url')

    if not url:
        return jsonify({'error': 'URL required'}), 400

    try:
        site_info_extractor = SiteInfoExtractor()
        text = site_info_extractor.get_site_info(url)
        return jsonify({'text': text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
