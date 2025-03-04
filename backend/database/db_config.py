from pymongo import MongoClient

# MongoDB Atlas connection string
MONGO_URI = "mongodb+srv://healthUser:strongpassword123@cluster0.mongodb.net/health-diagnostics-db?retryWrites=true&w=majority"

client = MongoClient(MONGO_URI)
db = client["health-diagnostics-db"]
reports_collection = db["health_reports"]
