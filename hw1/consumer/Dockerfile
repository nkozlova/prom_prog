FROM ubuntu:16.04

RUN apt-get update
RUN apt-get install -y sqlite3 libsqlite3-dev
RUN apt-get install -y python3-pip && pip3 install pika
RUN apt-get install -y rabbitmq-server

ADD consumer.py /
CMD [ "tail -F /dev/null" ]
