import pika, random, mysql.connector, json
from db import dbConnect


##get rabbitmq connection
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

##get random number between 1 and 10
random_number = random.randint(2, 9)

##get the result_1 value from random number
result_1 = ''
for x in range(random_number):
    result_1 = result_1 + str(x+1)

###connect db and insert the values
conn = dbConnect.connectDB(self=None)
mycursor = conn.cursor()

sql = "INSERT INTO random_results (random_number, result_1) VALUES (%s, %s)"
val = (random_number, result_1)
mycursor.execute(sql, val)

conn.close()

### end insert query

print("Random Number is :"+str(random_number))
print("result_1 value is :"+str(result_1))

message = {"id": mycursor.lastrowid, "text": result_1}
channel.basic_publish(exchange='', routing_key='hello', body=json.dumps(message))
print(" [x] Sent this value "+ result_1+" consumer")
connection.close()
