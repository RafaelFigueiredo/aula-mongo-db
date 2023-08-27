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
    time_serie = {}
    for key in storage:
        # lembra que nossa key é o timestamp
        telemetry = storage[key]
        print(f'telemetry: {telemetry}')

        # no query estamos interessados em apenas um unico attributo
        value = telemetry[attribute]
        time_serie[key] = value
    
    result = {
        'attribute': attribute,
        'data': time_serie
    }
    return result