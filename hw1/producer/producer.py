#!/usr/bin/env python3
import pika


connection = pika.BlockingConnection(
    pika.URLParameters("amqp://guest:guest@rabbit:5672"))
channel = connection.channel()

channel.queue_declare(queue='hello')

try:
    while True:
        mail = input('Write your message this: ')
        channel.basic_publish(exchange='',
                              routing_key='hello',
                              body=mail)
        print('Sented your mail')

except KeyboardInterrupt:
    exit()
