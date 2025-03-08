from backend.database.db_config import users_collection, reports_collection

def save_user(data):
    """Save user information to the database"""
    if user := users_collection.find_one({"email": data["email"]}):
        return "User already exists"
    users_collection.insert_one(data)
    return "User registered successfully"

def save_report(user_email, report_data):
    """Save report analysis to the database"""
    report = {
        "email": user_email,
        "report": report_data
    }
    reports_collection.insert_one(report)
    return "Report saved successfully"

def get_reports(user_email):
    """Retrieve all reports for a specific user"""
    reports = reports_collection.find({"email": user_email})
    return list(reports)
