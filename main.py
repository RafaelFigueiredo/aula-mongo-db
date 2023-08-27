from flask import Flask

app = Flask(__name__)

@app.post("/telemetry")
def post_telemetry():
    
    return {
        'ok': True
    }