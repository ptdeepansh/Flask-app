from flask import Flask, request, abort, jsonify
from flask_cors import CORS
import pymongo
from dotenv import load_dotenv 
import os

load_dotenv()

Mongo_URI = os.getenv('MONGODB_URI')

client = pymongo.MongoClient(Mongo_URI)

db = client.DeepCloud

collection = db['learning-project']

app = Flask(__name__)
CORS(app)

@app.route("/submit", methods=["POST"])
def submitData():
    data = dict(request.form)
    age = int(data.get('age'))
    if age < 18:
        return jsonify({
            "success": False,
            "error": "You are not allowed to submit your details!"
        }), 403
    
    collection.insert_one(data)

    return jsonify({
        "success": True,
        "redirect": "http://127.1.0.4:9080/submitted"
    }), 201


@app.route("/submitted")
def submitted():
    return "Data submitted successfully!"

if __name__ == '__main__':
    app.run(host='127.1.0.4', port=9080, debug=True)
