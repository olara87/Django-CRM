import os
import mysql.connector

dataBase = mysql.connector.connect(
    host = os.environ.get('HOST'),
    user = os.environ.get('USER'),
    passwd = os.environ.get('PASSWD'),
)

cursorObject = dataBase.cursor()

cursorObject.execute('CREATE DATABASE myDB CHARACTER SET utf8')

print('All done!')