from flask import Flask, request, jsonify
app = Flask(__name__)
current = {"light": 0}

@app.route("/update", methods=["POST"])
def update():
    current["light"] = request.json["light"]
    return "ok"

@app.route("/latest")
def latest():
    return jsonify(current)
