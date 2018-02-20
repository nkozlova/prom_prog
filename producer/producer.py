#!/usr/bin/env python3
import pika


connection = pika.BlockingConnection(
    pika.URLParameters("amqp://guest:guest@rabbit:5672"))
channel = connection.channel()

channel.queue_declare(queue='hello')

try:
    while True:
        mail = input('[*] Enter your message: ')
        channel.basic_publish(exchange='',
                              routing_key='hello',
                              body=mail)
        print('[x] Sent!')
except KeyboardInterrupt:
    connection.close()
