from flask import jsonify, request
from db.db import cnx

cur = cnx.cursor()

class Device:
    
    def list():
        return {}, 200

    def create(body):
        return {}, 200

