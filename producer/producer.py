#!/usr/bin/env python
import pika


connection = pika.BlockingConnection(pika.ConnectionParameters(
	host='rabbitmq'))
channel = connection.channel()

channel.queue_declare(queue='hello')

while True:
    mail = input("Enter your message: ")
    channel.basic_publish(exchange='',
                            routing_key='hello',
                            body=mail)

connection.close()
