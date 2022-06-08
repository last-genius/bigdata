FROM python:3.9-slim

RUN pip install --upgrade pip
RUN pip install flask
RUN pip install cassandra-driver

WORKDIR /hw8
COPY rest/app.py .
COPY kafka-cassandra/cassandra_client.py .

CMD ["python3", "app.py"]