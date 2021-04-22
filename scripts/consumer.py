import pika, sys, os, mysql.connector, json
from db import dbConnect

def main(connect_db=None):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    def callback(ch, method, properties, body):
        json_object = json.loads(body)
        text = json_object['text']
        id = json_object['id']
        print(" [x] Received %r" % text)

        ###logic for reverse the result_1 what received from producer
        result_2 = text[::-1]

        ###update the result_2 value
        mycursor = connect_db.cursor()
        sql = "UPDATE random_results SET result_2 = %s WHERE id = %s"
        val = (result_2, id)
        mycursor.execute(sql, val)
        ### end update query



    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        connect_db = dbConnect.connectDB(self=None)
        main(connect_db)
        connect_db.close()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
