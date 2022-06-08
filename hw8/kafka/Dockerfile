FROM python:3.9-slim

RUN pip install --upgrade pip
RUN pip install kafka-python

WORKDIR /hw8

COPY ./kafka/kafka_write.py .
COPY ./PS_20174392719_1491204439457_log.csv .

CMD ["python3", "kafka_write.py"]
