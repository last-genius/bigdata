from json import loads
from kafka import KafkaConsumer
from cassandra_client import CassandraClient


consumer = KafkaConsumer('topic-kafka',
                         bootstrap_servers='kafka-server:9092',
                         value_deserializer=lambda x: loads(x.decode('ascii')))

client = CassandraClient('cassandra-server', 9042, 'hw8')
client.connect()

for msg in consumer:
    print('sent')
    client.insert_into_user_fraud(
        [msg.value['nameOrig'], msg.value['isFraud'], msg.value['amount'], msg.value['transaction_date']])
    client.insert_into_user_top(
        [msg.value['nameOrig'], msg.value['amount'], msg.value['transaction_date']])
    client.insert_into_user_incoming(
        [msg.value['nameDest'], msg.value['amount'], msg.value['transaction_date']])

client.session.shutdown()
