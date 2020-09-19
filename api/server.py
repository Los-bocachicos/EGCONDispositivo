from flask import Flask, jsonify, request
from flask_cors import CORS
from controllers.device import Device

app = Flask("EG-CON-Device")
CORS(app)

@app.route('/device', methods=['GET'])
def getAll():
    return Device.list()

@app.route('/device', methods=['POST'])
def post():
    body = request.json1
    return Device.create(body)

app.run(port=8080,debug=True)