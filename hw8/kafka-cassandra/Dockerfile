FROM python:3.9-slim

RUN pip install --upgrade pip
RUN pip install kafka-python
RUN pip install cassandra-driver

WORKDIR /hw8
COPY kafka-cassandra/kafka-cassandra.py .
COPY kafka-cassandra/cassandra_client.py .

CMD ["python3", "kafka-cassandra.py"]