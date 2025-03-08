from pymongo import MongoClient

# MongoDB Atlas connection string
MONGO_URI = "mongodb+srv://healthUser:strongpassword123@health-diagnostics-db.stifb.mongodb.net/?retryWrites=true&w=majority&appName=health-diagnostics-db"

client = MongoClient(MONGO_URI)
db = client["health-diagnostics-db"]
reports_collection = db["health_reports"]
