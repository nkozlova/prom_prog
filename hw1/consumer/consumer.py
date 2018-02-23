#!/usr/bin/env python3
import pika
import sqlite3


queue_connection = pika.BlockingConnection(
    pika.URLParameters("amqp://guest:guest@rabbit:5672"))
channel = queue_connection.channel()
channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print('Received mail: ', body)
    cursor.execute('INSERT INTO Mails (message) VALUES (?)', (body,))
    db_connection.commit()
    print('INSERT was successful')

db_connection = sqlite3.connect('messages.db')
cursor = db_connection.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS Mails (message VARCHAR(256))')

channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

try:
    channel.start_consuming()

except KeyboardInterrupt:
    cursor.execute('SELECT * FROM Mails LIMIT 3')
    print(cursor.fetchall())
    print('This is TOP 3 rows from database')
    channel.stop_consuming()

db_connection.close()
channel.close()

