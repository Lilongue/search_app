from flask import Flask, request, jsonify
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os
import tempfile

app = Flask(__name__)

@app.route('/scrape', methods=['POST'])
def scrape():
    url = request.json.get('url')
    if not url:
        return jsonify({'error': 'URL required'}), 400

    try:
        # Create temporary user data directory
        user_data_dir = tempfile.mkdtemp()
        driver_path = os.environ.get('CHROMEDRIVER_PATH', '/usr/local/bin/chromedriver')
        options = webdriver.ChromeOptions()
        options.add_argument(f'--user-data-dir={user_data_dir}')
        options.add_argument('user-agent=Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19')
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        driver = webdriver.Chrome(service=Service(driver_path), options=options)
        driver.get(url)
        html = driver.page_source
        return jsonify({'html': html})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        driver.quit()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
