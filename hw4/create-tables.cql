CREATE KEYSPACE hw4 WITH REPLICATION = {'class' : 'SimpleStrategy', 'replication_factor' : 1 };

USE hw4;

DROP TABLE IF EXISTS reviews_for_product_id;
DROP TABLE IF EXISTS reviews_for_product_rating;
DROP TABLE IF EXISTS reviews_for_customer;
DROP TABLE IF EXISTS most_reviewed_date;
DROP TABLE IF EXISTS most_active_customers;

CREATE TABLE reviews_for_product_id
(
    product_id text,
	review_id text,
    review_headline text,
    review_body text,
	review_date date,
    PRIMARY KEY ((product_id), review_id)
);

CREATE TABLE reviews_for_product_rating
(
    product_id text,
    review_id text,
    star_rating int,
    review_headline text,
    review_body text,
    review_date date,
	PRIMARY KEY ((product_id, star_rating), review_id)
);

CREATE TABLE reviews_for_customer
(
	customer_id text,
    product_id text,
    review_id text,
    review_headline text,
    review_body text,
    review_date date,
    PRIMARY KEY ((customer_id), product_id)
);

CREATE TABLE most_reviewed_date
(
    review_date date,
    product_id text,
	star_rating int,
	product_title text,
    PRIMARY KEY ((review_date), product_id, star_rating)
);

CREATE TABLE most_active_customers
(
    review_date date,
	star_rating int,
    customer_id text,
    PRIMARY KEY (review_date, star_rating, customer_id)
);