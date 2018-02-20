FROM python:3

RUN pip install --upgrade pip
RUN pip install pika
RUN pip install psycopg2

ADD consumer.py consumer.py

CMD [ "python", "consumer.py" ]
