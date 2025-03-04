from pymongo import MongoClient
import os

# MongoDB Atlas connection (free tier)
MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://<your_username>:<your_password>@cluster0.mongodb.net/health-diagnostics?retryWrites=true&w=majority")
client = MongoClient(MONGO_URI)

db = client.get_database("health-diagnostics")
users_collection = db.get_collection("users")
reports_collection = db.get_collection("reports")
    