from flask import Flask, request, jsonify
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

app = Flask(__name__)

@app.route('/scrape', methods=['POST'])
def scrape():
    url = request.json.get('url')
    if not url:
        return jsonify({"error": "URL required"}), 400

    try:
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')  # Run in background
        driver = webdriver.Chrome(service=Service(), options=options)
        driver.get(url)
        time.sleep(5)  # Wait for page load
        html = driver.page_source  # Get raw HTML
        driver.quit()
        return jsonify({"html": html})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

