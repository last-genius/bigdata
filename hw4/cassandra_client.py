from cassandra.cluster import Cluster
from cassandra.query import dict_factory


class CassandraClient:
    def __init__(self, host, port, keyspace):
        self.host = host
        self.port = port
        self.keyspace = keyspace
        self.session = None

    def connect(self):
        cluster = Cluster([self.host], port=self.port)
        self.session = cluster.connect(self.keyspace)
        self.session.row_factory = dict_factory

    def insert_reviews_for_product_id(self, data):
        self.session.execute(f"INSERT INTO reviews_for_product_id (product_id, review_id, review_headline, review_body, review_date)"
                             f"VALUES ('{data[0]}', '{data[1]}', '{data[2]}', '{data[3]}', '{data[4]}')")

    def insert_reviews_for_product_rating(self, data):
        self.session.execute(f"INSERT INTO reviews_for_product_rating (product_id, review_id, star_rating, review_headline, review_body, review_date)"
                             f"VALUES ('{data[0]}', '{data[1]}', {round(data[2])}, '{data[3]}', '{data[4]}', '{data[5]}')")

    def insert_reviews_for_customer(self, data):
        self.session.execute(f"INSERT INTO reviews_for_customer (customer_id, product_id, review_id, review_headline, review_body, review_date)"
                             f"VALUES ('{data[0]}', '{data[1]}', '{data[2]}', '{data[3]}', '{data[4]}', '{data[5]}')")

    def insert_most_reviewed_date(self, data):
        self.session.execute(f"INSERT INTO most_reviewed_date (review_date, product_id, star_rating, product_title)"
                             f"VALUES ('{data[0]}', '{data[1]}', {round(data[2])}, '{data[3]}')")

    def insert_most_active_customers(self, data):
        self.session.execute(f"INSERT INTO most_active_customers (review_date, customer_id, star_rating)"
                             f"VALUES ('{data[0]}', '{data[1]}', {round(data[2])})")

    def select_reviews_for_product_id(self, data):
        product_id = data['product_id']
        query = f"SELECT * FROM reviews_for_product_id WHERE product_id = '{product_id}';"
        return list(self.session.execute(query))

    def select_reviews_for_product_rating(self, data):
        product_id = data['product_id']
        star_rating = data['star_rating']
        query = f"SELECT * FROM reviews_for_product_rating " \
                f"WHERE product_id = '{product_id}' AND star_rating = {star_rating};"
        return list(self.session.execute(query))

    def select_reviews_for_customer(self, data):
        customer_id = data['customer_id']
        query = f"SELECT * FROM reviews_for_customer WHERE customer_id = '{customer_id}';"
        return list(self.session.execute(query))

    def select_most_reviewed_date(self, data):
        start_date = data['start_date']
        end_date = data['end_date']
        N = data['N']
        query = f"SELECT product_id, product_title, COUNT(*) from most_reviewed_date " \
                f"WHERE (review_date >= '{start_date}') " \
                f"AND (review_date < '{end_date}') LIMIT {N} ALLOW FILTERING;"
        lst = list(self.session.execute(query))
        lst.sort(key=lambda d: d['count'], reverse=True)
        return lst

    def select_most_productive_customers(self, data):
        start_date = data['start_date']
        end_date = data['end_date']
        N = data['N']
        query = f"SELECT customer_id, COUNT(*) from most_active_customers " \
                f"WHERE (review_date >= '{start_date}') " \
                f"AND (review_date < '{end_date}') LIMIT {N} ALLOW FILTERING;"
        lst = list(self.session.execute(query))
        lst.sort(key=lambda d: d['count'], reverse=True)
        return lst

    def select_haters(self, data):
        start_date = data['start_date']
        end_date = data['end_date']
        N = data['N']
        query = f"SELECT customer_id from most_active_customers " \
                f"WHERE (review_date >= '{start_date}') " \
                f"AND (review_date < '{end_date}') AND (star_rating < 3) " \
                f"LIMIT {N} ALLOW FILTERING;"
        return list(self.session.execute(query))

    def select_backers(self, data):
        start_date = data['start_date']
        end_date = data['end_date']
        N = data['N']
        query = f"SELECT customer_id from most_active_customers " \
                f"WHERE (review_date >= '{start_date}') " \
                f"AND (review_date < '{end_date}') AND (star_rating >= 3) " \
                f"LIMIT {N} ALLOW FILTERING;"
        return list(self.session.execute(query))
