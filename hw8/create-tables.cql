CREATE KEYSPACE hw8 WITH REPLICATION = {'class' : 'SimpleStrategy', 'replication_factor' : 1 };
USE hw8;

DROP TABLE IF EXISTS user_fraud;
DROP TABLE IF EXISTS user_top;
DROP TABLE IF EXISTS user_incoming;

CREATE TABLE IF NOT EXISTS user_fraud
(
    uid text,
    isFraud int,
    amount float,
    transaction_date date,
    PRIMARY KEY (uid, isFraud)
);

CREATE TABLE IF NOT EXISTS user_top
(
    uid text,
    amount float,
    transaction_date date,
    PRIMARY KEY (uid, amount)
);

CREATE TABLE IF NOT EXISTS user_incoming
(
    uid text,
    amount float,
    transaction_date date,
    PRIMARY KEY (uid, transaction_date)
);