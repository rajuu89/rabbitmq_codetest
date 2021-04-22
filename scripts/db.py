import mysql.connector
from decouple import config

class dbConnect:

    host = config('DB_HOST')
    uname = config('DB_USER')
    password = config('DB_PASSWORD')
    database = config('DB_DATABASE')

    def getConnection(self):

        host = dbConnect.host
        uname = dbConnect.uname
        password = dbConnect.password

        try:
            mydb = mysql.connector.connect(host=host, user=uname, password=password)

            return mydb

        except:
            print("CONNECTION ERROR")
            exit(1)


    def connectDB(self):

        host = dbConnect.host
        uname = dbConnect.uname
        password = dbConnect.password
        database = dbConnect.database

        try:
            mydb = mysql.connector.connect(host=host, user=uname, password=password, database=database)

            return mydb

        except:
            print("CONNECTION ERROR")
            exit(1)
