from flask import Flask, render_template, request, jsonify
import requests
from flask_cors import CORS

app = Flask("Web Device", template_folder='templates', static_folder='static')
CORS(app)
locations = ['SOUTH', 'NORTH', 'EAST', 'WEST']
sensor_types = ['SENSOR', 'ACTUATOR']


@app.route('/listDevices', methods=['GET'])
def list_devices():
    devices = requests.get('http://localhost:8080/api/device').json()
    return render_template('listDevice.html', devices=devices)


@app.route('/createDevice', methods=['GET'])
def create_device():
    return render_template('createDevice.html', locations=locations, sensor_types=sensor_types)


@app.route('/saveDevice', methods=['POST'])
def save_device():
    # print(dict(request.values))
    # return jsonify(request.values)
    return list_devices()


app.run(port=5000, host='0.0.0.0', debug=True)
