FROM python:3.9-slim

RUN pip install --upgrade pip
RUN pip install kafka-python

WORKDIR /hw6
COPY ./kafka_stream.py .
COPY ./twcs.csv .

CMD ["python3", "kafka_stream.py"]
