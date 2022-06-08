FROM python:3.9-slim

RUN pip install --upgrade pip
RUN pip install cassandra-driver
RUN pip install flask

COPY ./cassandra_client.py .
COPY ./app.py .

CMD ["python3", "app.py"]