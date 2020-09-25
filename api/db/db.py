import mysql.connector as mysql
import os

cnx = mysql.MySQLConnection(
    host="172.17.0.2",
    port=3306,
    user="root",
    password=os.getenv('DB_PASSWORD'),
    database="EGCON",
    auth_plugin='mysql_native_password'
)