from pickle import TRUE
from flask import Flask, jsonify

app = Flask(__name__)
@app.route("/")
def greet():
    return "hello mam"

db = [
    {
        "name": "Alexa",
        "rollno": 20
    },
    {
        "name": "Sumukhi",
        "rollno": 39
    }
]

@app.route("/get", methods = ["GET"])
def get():
    return jsonify({"data": db})

@app.route("/db", methods = ["POST"])
def post():
    st3 = {"name": "siya",
            "rollno": 38}
    db.append(st3)
    return jsonify({"data":db})

app.run(debug = True)