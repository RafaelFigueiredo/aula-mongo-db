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
    body = request.get_json()
    begin = datetime.fromisoformat(body['begin'])
    end = datetime.fromisoformat(body['end'])

    time_serie = {}
    for key in storage:
        # lembra que nossa key é o timestamp
        timestamp = datetime.fromisoformat(key)
        
        # ignora resultados anteriores a nossa janela de interesse
        if timestamp < begin:
            continue
        
        # ignora results posteriores a nossa janela de interesse
        if timestamp > end:
            continue

        telemetry = storage[key]
        print(f'telemetry: {telemetry}')

        # no query estamos interessados em apenas um unico attributo
        value = telemetry[attribute]
        time_serie[key] = value
    
    result = {
        'attribute': attribute,
        'query': {
            'begin': begin,
            'end': end
        },
        'data': time_serie
    }
    return result