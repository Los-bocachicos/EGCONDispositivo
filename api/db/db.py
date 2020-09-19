import mysql.connector as mysql

cnx = mysql.MySQLConnection(
    host="172.17.0.2",
    port=3306,
    user="root",
    password="passw0rd",
    database="EGCON",
    auth_plugin='mysql_native_password'
)