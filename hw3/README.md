### Products table

* product_id - partition key
* star_rating - clustering key

To sort reviews by stars inside partitions, and to efficiently search with product_id
provided (as in the first queries), to split them between different clusters and
avoid sending unnecessary queries to clusters that do not have the data, in Cassandra
you can only use partition keys with equalities, not to sort data (to avoid data filtering).

### Customers table

* customer_id - partition key
* star_rating - clustering

Because in the latter queries, we need to efficiently search with customer_id provided,
and to compare star_ratings we need to sort entries inside the cluster
