from tracemalloc import start
from cassandra.cluster import Cluster


class CassandraClient:
    def __init__(self, host, port, keyspace):
        self.host = host
        self.port = port
        self.keyspace = keyspace
        self.session = None

    def connect(self):
        cluster = Cluster([self.host], port=self.port)
        self.session = cluster.connect(self.keyspace)

    def insert_into_user_fraud(self, row):
        self.session.execute(f"INSERT INTO user_fraud (uid, isFraud, amount, transaction_date) "
                             f"VALUES ('{row[0]}', {row[1]}, {row[2]}, '{row[3]}')")

    def insert_into_user_top(self, row):
        self.session.execute(f"INSERT INTO user_top (uid, amount, transaction_date) "
                             f"VALUES ('{row[0]}', {row[1]}, '{row[2]}')")

    def insert_into_user_incoming(self, row):
        self.session.execute(f"INSERT INTO user_incoming (uid, amount, transaction_date) "
                             f"VALUES ('{row[0]}', {row[1]}, '{row[2]}');")

    def select_user_fraud(self, data):
        uid = data['uid']
        query = f"SELECT * from user_fraud WHERE uid = '{uid}' AND isFraud = 1;"
        return list(self.session.execute(query))

    def select_user_top(self, data):
        uid = data['uid']
        query = f"SELECT * from user_top WHERE uid = '{uid}' ORDER BY amount DESC LIMIT 3;"
        return list(self.session.execute(query))

    def select_user_incoming(self, data):
        uid = data['uid']
        start_date = data['start_date']
        end_date = data['end_date']
        query = f"SELECT SUM(amount) from user_incoming WHERE uid = '{uid}' " \
                f"AND (transaction_date >= '{start_date}') AND (transaction_date <= '{end_date}'); "
        return list(self.session.execute(query))
