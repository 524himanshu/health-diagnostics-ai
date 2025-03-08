from flask import Blueprint, request, jsonify
import PyPDF2
import re

reports_bp = Blueprint('reports', __name__)

@reports_bp.route('/test', methods=['GET'])
def test_reports():
    return jsonify({'message': 'Reports route working'})

@reports_bp.route('/', methods=['POST'])
def analyze_report():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    reader = PyPDF2.PdfReader(file)
    report_text = "".join(page.extract_text() for page in reader.pages if page and page.extract_text())

    # Extract medical values using regex
    hemoglobin = re.search(r'Hemoglobin\s+(\d+\.\d+)\s+g/dL', report_text)
    glucose = re.search(r'Glucose\s+(\d+\.\d+)\s+mg/dL', report_text)
    rbc = re.search(r'Total RBC\s+(\d+\.\d+)\s+X 10\^6/µL', report_text)
    platelets = re.search(r'Platelet Count\s+(\d+)\s+X 10³ / µL', report_text)

    results = {
        "Hemoglobin": hemoglobin[1] if hemoglobin else "Not found",
        "Glucose": glucose[1] if glucose else "Not found",
        "Total RBC": rbc[1] if rbc else "Not found",
        "Platelet Count": platelets[1] if platelets else "Not found"
    }

    recommendations = []

    if hemoglobin and float(hemoglobin[1]) < 13.0:
        recommendations.append("Low hemoglobin detected. Consider iron supplementation and consult a doctor.")
    if glucose and float(glucose[1]) > 120.0:
        recommendations.append("High glucose levels detected. Monitor your diet and consult an endocrinologist.")
    if rbc and float(rbc[1]) > 5.5:
        recommendations.append("Elevated RBC count. Suggest consulting a hematologist for further evaluation.")
    if platelets and int(platelets[1]) > 410:
        recommendations.append("High platelet count detected. Possible inflammation or other underlying condition — consult a specialist.")

    return jsonify({"results": results, "recommendations": recommendations})
