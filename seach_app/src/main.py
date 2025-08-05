from flask import Flask, request, jsonify

from ya_search import YaSearch

app = Flask(__name__)


@app.route('/search', methods=['POST'])
def search():
    query_text = request.json.get('query_text')
    folder_id = request.json.get('folder_id')
    page_size = request.json.get('page_size', 10)
    api_key = request.json.get('api_key')
    ya_search = YaSearch(api_key)
    results = ya_search.search(query_text, folder_id, page_size)
    return jsonify({"results": results})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5020)
