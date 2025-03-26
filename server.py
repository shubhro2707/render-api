from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

DATA_FILE = "sensor_data.json"

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Render API is running!"})

@app.route("/upload", methods=["POST"])
def upload_data():
    if "file" not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files["file"]
    data = json.loads(file.read().decode("utf-8"))  # Proper JSON parsing

    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

    return jsonify({"message": "Sensor data saved successfully!"})

if __name__ == "__main__":
    app.run(debug=True)
