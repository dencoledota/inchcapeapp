from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200

@app.route('/', methods=['GET'])
def get_posts():
    try:
        response = requests.get('https://jsonplaceholder.typicode.com/posts')
        response.raise_for_status()
        posts = response.json()
        return jsonify(posts)
    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Unable to fetch posts"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
