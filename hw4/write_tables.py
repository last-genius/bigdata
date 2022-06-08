import pandas as pd
from cassandra_client import CassandraClient

df = pd.read_csv('amazon_reviews_us_Books_v1_02.tsv', sep='\t', nrows=1000)

df['review_headline'] = df['review_headline'].str.replace("'", '"')
df['review_body'] = df['review_body'].str.replace("'", '"')
df['product_title'] = df['product_title'].str.replace("'", '"')
df.dropna(inplace=True)

cassandra = CassandraClient('localhost', 9042, 'hw4')
cassandra.connect()

for idx, row in df.iterrows():
    cassandra.insert_reviews_for_product_id([row['product_id'], row['review_id'], row['review_headline'],
                                            row['review_body'], row['review_date']])

    cassandra.insert_reviews_for_product_rating([row['product_id'], row['review_id'], row['star_rating'],
                                                row['review_headline'], row['review_body'], row['review_date']])

    cassandra.insert_reviews_for_customer([row['customer_id'], row['product_id'], row['review_id'],
                                          row['review_headline'], row['review_body'], row['review_date']])

    cassandra.insert_most_reviewed_date([row['review_date'], row['product_id'], row['star_rating'],
                                        row['product_title']])

    cassandra.insert_most_active_customers(
        [row['review_date'], row['customer_id'], row['star_rating']])

cassandra.session.shutdown()
