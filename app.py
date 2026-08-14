from flask import Flask, jsonify
import time

app = Flask(__name__)
status = "IDLE"
@app.route("/start", methods=["POST"])
def start():
    global status
    status = "RUNNING"
    return jsonify({"status": "started"})

@app.route("/status")
def get_status():
    return jsonify({"status": status})

app.run(host="0.0.0.0", port=5000)
