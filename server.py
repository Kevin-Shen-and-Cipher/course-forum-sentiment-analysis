from flask import Flask, request, jsonify
from utils import config, sentiment_analysis

app = Flask(__name__)
_IP = config.get_ip()
_PORT = config.get_port()

@app.route('/get_emotional_score', methods=['POST'])
def get_emotional_score():
    content = request.get_json()
    try:
        text = content['text']
        http_code, data = sentiment_analysis.get_emotional_score(text)
        return jsonify(data), http_code
    except KeyError as error:
        error_message = f"Missing required key: {error}"
        return jsonify({'error': error_message}), 400

if __name__ == "__main__":
    app.run(debug=True, host=_IP, port=_PORT)
