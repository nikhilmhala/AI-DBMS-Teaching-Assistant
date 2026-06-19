from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

LANGFLOW_URL = "http://localhost:7860/api/v1/run/d0830fd7-4ee6-4bec-887c-8914543820bc?stream=false"


API_KEY = "sk-LjYE_cKhpleNsmSUZxxbpzpH2amaua6AxPseu1wG2es"

@app.route("/chat", methods=["POST"])
def chat():

    user_message = request.json.get("message", "")

    response = requests.post(
        LANGFLOW_URL,
        headers={
            "Content-Type": "application/json",
            "x-api-key": API_KEY
        },
        json={
            "output_type": "chat",
            "input_type": "chat",
            "input_value": user_message
        }
    )

    return jsonify(response.json())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)