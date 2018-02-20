import pika
import psycopg2 as ps


connection = pika.BlockingConnection(#pika.ConnectionParameters(
#	host='queue', port=5672))

pika.URLParameters(
	"amqp://guest:guest@queue:5672"))
channel = connection.channel()

db = ps.connect(
	database='db_hello', 
	user='login', 
	password='pass', 
	host='database')
cursor.execute("DROP TABLE IF EXISTS Mails;")
connection.commit()
cursor.close

cursor.execute("CREATE TABLE Mails (mail VARCHAR(256));")
connection.commit()
cursor.close

#text = dp.prepare("INSERT INTO Mails VALUES($1);")

def callback(ch, method, properties, body):
    #text(body)
    cursor = db.cursor()
    command = "INSERT INTO Mails VALUES(" + body + ");"
    cursor.execute(command)
    connection.commit()
    cursor.close

channel.queue_declare(queue='hello')

channel.basic_consume(callback, 
			queue='hello', 
			no_ack=True)

channel.start_consuming()

