FROM ubuntu

ADD requirements.txt requirements.txt
RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y python3-pip
RUN pip3 install -r requirements.txt

ADD consumer.py consumer.py

ENTRYPOINT python3 consumer.py
