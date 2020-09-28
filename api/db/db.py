import mysql.connector as mysql
import os


def get_connection():
    cnx = mysql.MySQLConnection(
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME'),
        auth_plugin='mysql_native_password'
    )
    return cnx
