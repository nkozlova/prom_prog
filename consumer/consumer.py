#!/usr/bin/env python
import pika
import postgresql
import time


time.sleep(20)
connection = pika.BlockingConnection(pika.ConnectionParameters(
	host='rabbitmq'))
channel = connection.channel()

db = postgresql.open('pq://docker:docker@database:5430/docker')
db.execute("DROP TABLE IF EXISTS Mails;")
db.execute("CREATE TABLE Mails (id INT PRIMARY KEY, mail VARCHAR(256));")
ins = db.prepare("INSERT INTO Mails (mail) VALUES ($1)")

channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    ins(str(body))

channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

channel.start_consuming()
