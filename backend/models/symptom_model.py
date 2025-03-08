from transformers import pipeline

# Load RoBERTa model for symptom classification
symptom_classifier = pipeline("text-classification", model="roberta-base")

def classify_symptoms(user_input):
    return symptom_classifier(user_input)
