from flask import jsonify, request
from db.db import cnx
import json as json_library


class Device:

    @staticmethod
    def serialize_params(row: tuple):
        if row[-1] is not None:
            row_copy = list(row)
            row_copy[-1] = json_library.loads(row_copy[-1])
            return tuple(row_copy)
        return row
    
    @staticmethod
    def list():
        respose = []
        cur = cnx.cursor()

        with cnx.cursor() as cur:
            cur.execute("SELECT * FROM device")
            rows = cur.fetchall()
            columns = [i[0] for i in cur.description]
            for row in rows:
                registry = zip(columns, Device.serialize_params(row))
                json = dict(registry)
                respose.append(json)
        return jsonify(respose), 200

    @staticmethod
    def create(body:dict):
        data = (body['name'], body['code'], body['type'], body['reference'], body['location'], json_library.dumps(body['params']),)
        sql = "INSERT INTO device (name, code, type, reference, location, params) VALUES(%s, %s, %s, %s, %s, %s);"
        with cnx.cursor() as cur:
            cur.execute(sql, data)
        cnx.commit()
        return {"status": "ok"}, 201

    @staticmethod
    def update(id:int, body:dict):
        data = []
        query = "UPDATE device SET "
        for value in body.keys():
            if value == "params":
                data.append(json_library.dumps(body[value]))
            else:
                data.append(body[value])
            query += value + "=%s, "
        query = query[:-2]
        query += " WHERE id=%s"
        data.append(int(id))
        print(data, query)
        with cnx.cursor() as cur:
            cur.execute(query, data)
        return {}, 200