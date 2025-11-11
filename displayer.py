from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
current = {"temperature": 0, "light": 0}

@app.route("/")
def home():
    return render_template("index.html", data=current)

@app.route("/update", methods=["POST"])
def update():
    data = request.json
    current["temperature"] = data.get("temperature", 0)
    current["light"] = data.get("light", 0)
    print("Updated:", current)
    return "OK"

@app.route("/latest")
def latest():
    return jsonify(current)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
