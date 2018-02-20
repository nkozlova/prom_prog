FROM ubuntu:16.04

RUN apt-get update && DEBIAN_FRONTEND=noninteractive \
    && apt-get install -y sqlite3 libsqlite3-dev

RUN apt-get install -y python3-pip 
RUN pip3 install pika
RUN apt-get install -y rabbitmq-server

ADD consumer.py consumer.py
