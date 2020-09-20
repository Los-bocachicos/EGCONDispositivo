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
    body = request.json
    return Device.create(body)

@app.route('/device/<device_id>', methods=['PUT'])
def put(device_id:int):
    body = request.json
    return Device.update(device_id, body)

@app.route('/device/<device_id>', methods=['DELETE'])
def delete(device_id:int):
    return Device.delete(device_id)

app.run(port=8080,debug=True, host="0.0.0.0")