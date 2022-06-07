from json import loads
from kafka import KafkaConsumer
import csv

consumer = KafkaConsumer('topic-tweets',
                         bootstrap_servers='kafka-server:9092',
                         value_deserializer=lambda x: loads(x.decode('ascii')))

last_time = ''
append_tweets = []

for tweet in consumer:
    if tweet.value['created_at'] != last_time:
        # write to file
        with open(f'tweets_{tweet.value["created_at"]}.csv', "w") as f:
            writer = csv.writer(f)
            writer.writerow(['author_id', 'created_at', 'text'])
            writer.writerows(append_tweets)
            append_tweets = []

        last_time = tweet.value['created_at']

    append_tweets.append(
        [tweet.value['author_id'], tweet.value['created_at'], tweet.value['text']])
