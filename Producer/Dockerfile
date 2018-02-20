FROM python:3

RUN pip install --upgrade pip
RUN pip install pika

ADD producer.py producer.py

CMD [ "python", "producer.py" ]
