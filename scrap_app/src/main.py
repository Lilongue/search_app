from flask import Flask, request, jsonify
from selenium_handler import SeleniumHandler
from employer_info import EmployerInfo
from siteInfoSearch import SiteInfoExtractor

app = Flask(__name__)
selenium_handler = SeleniumHandler()

@app.route('/scrape', methods=['POST'])
def scrape():
    """
    HTTP endpoint to handle web scraping requests
    
    Expected JSON payload:
    {
        "url": "https://example.com"
    }
    
    Returns:
        JSON response with HTML content or error message
    """
    url = request.json.get('url')
    if not url:
        return jsonify({'error': 'URL required'}), 400

    try:
        employer_info = EmployerInfo()
        employer_info.phone = "8 (921) 962-15-09"
        employer_info.site = "nastroenie-dental.ru"
        employer_info.organization_name = "ООО \"Настроение\""
        site_info_extractor = SiteInfoExtractor()
        html = site_info_extractor.get_site_info(url)
        return jsonify({'html': html})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
