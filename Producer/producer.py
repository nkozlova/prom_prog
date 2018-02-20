import sys
import pika


connection = pika.BlockingConnection(#pika.ConnectionParameters(
#	host='queue', port=5672))
pika.URLParameters(
	"amqp://guest:guest@localhost:5672"))

channel = connection.channel()
channel.queue_declare(queue='hello')

mail = ' '.join(sys.argv[1:])
channel.basic_publish(
	exchange='', 
	routing_key='hello', 
	body=mail)

connection.close()
