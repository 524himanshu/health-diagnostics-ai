from transformers import pipeline

# Load RoBERTa model for symptom classification
symptom_classifier = pipeline("text-classification", model="roberta-base")

def classify_symptoms(user_input):
    result = symptom_classifier(user_input)
    return result
