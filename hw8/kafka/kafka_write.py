from time import sleep
from json import dumps
from kafka import KafkaProducer
import datetime
from csv import DictReader
import random

producer = KafkaProducer(bootstrap_servers=['kafka-server:9092'],
                         value_serializer=lambda x: dumps(x).encode('ascii'))

with open('./PS_20174392719_1491204439457_log.csv', 'r') as f:
    reader = DictReader(f)
    for line in reader:
        sleep(0.05)
        producer.send('topic-kafka', {'type': line['type'],
                                      'amount': line['amount'],
                                      'nameOrig': line['nameOrig'],
                                      'oldbalanceOrg': line['oldbalanceOrg'],
                                      'nameDest': line['nameDest'],
                                      'isFraud': line['isFraud'],
                                      'transaction_date': (datetime.date.today() -
                                                           datetime.timedelta(days=random.randint(1, 30))).strftime("%Y-%m-%d")})

    producer.flush()
