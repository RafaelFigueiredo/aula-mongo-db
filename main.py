from flask import Flask, request
from flask_pymongo import PyMongo
from datetime import datetime

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://root:swordfish@localhost:27017/my_app?authSource=admin"
mongo = PyMongo(app)

storage = {}


@app.post("/telemetry")
def post_telemetry():
    telemetry = request.get_json()

    # add timestamp
    telemetry['timestamp'] = datetime.utcnow()

    print(telemetry)
    mongo.db.telemetry.insert_one(telemetry)
    return {
        'ok': True
    }

@app.get("/query/<attribute>")
def get_attribute(attribute):
    body = request.get_json()
    begin = datetime.fromisoformat(body['begin'])
    end = datetime.fromisoformat(body['end'])

    filter={
        'timestamp': {
            '$gte': begin, 
            '$lte': end
        }
    }

    storage = mongo.db.telemetry.find(
        filter=filter
    )
    
    time_serie = {}
    for telemetry in storage:
        print(telemetry)
        key = telemetry['timestamp'].isoformat()
        
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