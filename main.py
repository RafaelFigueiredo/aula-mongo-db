from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.post("/telemetry")
def post_telemetry():
    telemetry = request.get_json()

    print(telemetry)
    return {
        'ok': True
    }