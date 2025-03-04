import PyPDF2
import re

def extract_report_data(file):
    reader = PyPDF2.PdfReader(file)
    report_text = ""

    for page in reader.pages:
        if page and page.extract_text():
            report_text += page.extract_text()

    # Extract medical values using regex
    hemoglobin = re.search(r'Hemoglobin\s+(\d+\.\d+)\s+g/dL', report_text)
    glucose = re.search(r'Glucose\s+(\d+\.\d+)\s+mg/dL', report_text)
    rbc = re.search(r'Total RBC\s+(\d+\.\d+)\s+X 10\^6/µL', report_text)
    platelets = re.search(r'Platelet Count\s+(\d+)\s+X 10³ / µL', report_text)

    results = {
        "Hemoglobin": hemoglobin.group(1) if hemoglobin else "Not found",
        "Glucose": glucose.group(1) if glucose else "Not found",
        "Total RBC": rbc.group(1) if rbc else "Not found",
        "Platelet Count": platelets.group(1) if platelets else "Not found"
    }

    # Analysis and recommendations
    recommendations = []
    if hemoglobin and float(hemoglobin.group(1)) < 13.0:
        recommendations.append("Low hemoglobin detected. Consider iron supplementation and consult a doctor.")
    if glucose and float(glucose.group(1)) > 120.0:
        recommendations.append("High glucose levels detected. Monitor your diet and consult an endocrinologist.")
    if rbc and float(rbc.group(1)) > 5.5:
        recommendations.append("Elevated RBC count. Suggest consulting a hematologist for further evaluation.")
    if platelets and int(platelets.group(1)) > 410:
        recommendations.append("High platelet count detected. Possible inflammation or other underlying condition — consult a specialist.")

    results["Recommendations"] = recommendations

    return results
