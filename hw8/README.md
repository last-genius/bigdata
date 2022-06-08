Launching the kafka instance, cassandra instance:

```
./run-kafka-cluster.sh
./run-cassandra-cluster.sh
```

Writing into kafka and from kafka into cassandra:

```
./kafka/run.sh
./kafka-cassandra/run.sh
```

And launching the REST server:
```
./rest/run.sh
```

The working kafka-cassandra pipeline:

![](./img/1.png)
![](./img/2.png)

Request 1

![](./img/3.png)

Request 2

![](./img/4.png)

Request 3

![](./img/5.png)
