from flask import Flask, request

app = Flask(__name__)

@app.post("/telemetry")
def post_telemetry():
    body = request.get_json()
    print(body)
    return {
        'ok': True
    }