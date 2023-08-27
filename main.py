from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

storage = {}


@app.post("/telemetry")
def post_telemetry():
    telemetry = request.get_json()

    # add timestamp
    telemetry['timestamp'] = datetime.utcnow().isoformat()

    print(telemetry)
    key = telemetry['timestamp']
    storage[key] = telemetry
    return {
        'ok': True
    }

@app.get("/query/<attribute>")
def get_attribute(attribute):
    return storage