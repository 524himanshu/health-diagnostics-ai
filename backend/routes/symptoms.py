import os
from dotenv import load_dotenv
import requests
from flask import Blueprint, request, jsonify

load_dotenv()

symptoms_bp = Blueprint('symptoms', __name__)

HUGGINGFACE_API_URL = "https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english"
HEADERS = {
    "Authorization": f"Bearer {os.getenv('HUGGINGFACE_API_KEY')}"
}


@symptoms_bp.route('/test', methods=['GET'])
def test_symptoms():
    return jsonify({'message': 'Symptoms route working'})


@symptoms_bp.route('/', methods=['POST'])
def analyze_symptoms():
    print("🚀 /api/symptoms route hit!")  # Debug log
    data = request.json
    user_input = data.get("symptoms")
    if not user_input:
            return jsonify({"error": "No symptoms provided"}), 400

    try:
        response = requests.post(HUGGINGFACE_API_URL, headers=HEADERS, json={"inputs": user_input})
        result = response.json()

        # Extract the top prediction
        prediction_label = result[0][0]['label']
        prediction_score = result[0][0]['score']

        follow_up = ""
        if "fever" in user_input.lower():
            follow_up = "How long have you had the fever? Do you also have chills or body aches?"
        elif "fatigue" in user_input.lower():
            follow_up = "Is the fatigue persistent or occasional? Are you getting enough sleep?"
        

        return jsonify({
            "prediction": prediction_label,
            "confidence": prediction_score,
            "follow_up": follow_up
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500
