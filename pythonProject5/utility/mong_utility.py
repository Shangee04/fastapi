from pymongo import MongoClient

Mongo_url = "mongodb://intern_23:intern%40123@192.168.0.220:2717/interns_b2_23"
client = "none"
try:
    client = MongoClient(Mongo_url)
    print("mongourl is connect")
except Exception as e:
    print("not connected" + str(e))

db = client.interns_b2_23
inventory = db.Shangeetha
