import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Centreville@101191',
)

cursorObject = dataBase.cursor()

cursorObject.execute('CREATE DATABASE elderco CHARACTER SET utf8')

print('All done!')