from db import dbConnect
from decouple import config

class Migrations:

    database = config('DB_DATABASE')

    def createDatabase(self):

        database = Migrations.database
        conn = dbConnect().getConnection()
        mycursor = conn.cursor()

        ## check table is exists or not
        mycursor.execute("SHOW DATABASES")
        dbnames = []
        for x in mycursor:
            dbnames.append(x[0])

        ###not exist table then create db
        if database not in dbnames:
            mycursor.execute("CREATE DATABASE "+database)
            print(database +" DATABASE CREATED SUCCESSFULLY")

        else:
            print(database +" DATABASE ALREADY EXISTS")

        conn.close()

    def createTable(self):
        conn = dbConnect().connectDB()
        mycursor = conn.cursor()

        ## check table is exists or not
        mycursor.execute("SHOW TABLES")
        dbtables = []
        for x in mycursor:
            dbtables.append(x[0])

        ###not exist table then create db
        if 'random_results' not in dbtables:
            mycursor.execute("CREATE TABLE random_results (id INT AUTO_INCREMENT PRIMARY KEY, random_number INT(2), result_1 VARCHAR(15), result_2 VARCHAR(15))")
            print("random_results TABLE CREATED SUCCESSFULLY")
            print("Migrations Completed")

        else:
            print("random_results TABLE ALREADY EXISTS")
            print("No Migrations")

        conn.close()

mo = Migrations()
### create db
mo.createDatabase()
### create db table
mo.createTable()
