from datetime import datetime
from json import dumps
from kafka import KafkaProducer
from csv import DictReader
from time import sleep

producer = KafkaProducer(bootstrap_servers='kafka-server:9092',
                         value_serializer=lambda x: dumps(x).encode('ascii'))

with open('twcs.csv', 'r') as f:
    reader = DictReader(f)
    for line in reader:
        producer.send('topic-tweets',
                      {'author_id': line['author_id'],
                       'created_at': datetime.now().strftime("%d_%m_%Y_%H_%M"),
                       'text': line['text']})
        sleep(0.05)

    producer.flush()
