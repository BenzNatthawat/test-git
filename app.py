from flask import Flask, request, abort, redirect, url_for, jsonify
import pymongo
import datetime
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

config = {
    "server": os.getenv("MONGO_SERVER", "127.0.0.1"),
}

connector = "mongodb://{}".format(config["server"])
client = pymongo.MongoClient(connector)
db = client["demo"]

@app.route("/", methods=['GET'])
def people():
    return "people"

@app.route("/mongo", methods=['GET'])
def mongo():
    return format(config["server"])

@app.route("/people", methods=['GET'])
def list_people():
    count = db.people.count_documents({})
    people = db.people.find({})
    result = []
    for person in people:
        result.append({
            "name": person.get("name"),
            "age": person.get("age"),
        })
    return jsonify({"count": count, "people": result})

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)