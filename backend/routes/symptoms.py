from flask import Blueprint, request, jsonify
from transformers import pipeline

symptoms_bp = Blueprint('symptoms', __name__)

# Symptom analysis pipeline
nlp = pipeline("text-classification", model="distilbert-base-uncased")

@symptoms_bp.route('/', methods=['POST'])
def analyze_symptoms():
    data = request.json
    user_input = data.get("symptoms")
    result = nlp(user_input)

    # Follow-up questions based on symptoms
    follow_up = ""
    if "fever" in user_input.lower():
        follow_up = "How long have you had the fever? Do you also have chills or body aches?"
    elif "fatigue" in user_input.lower():
        follow_up = "Is the fatigue persistent or occasional? Are you getting enough sleep?"

    return jsonify({"prediction": result, "follow_up": follow_up})
