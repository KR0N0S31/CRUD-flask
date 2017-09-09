from pymongo import MongoClient

mongoClient = MongoClient('localhost',27017)
db = mongoClient.Logs
collection = db.logs
