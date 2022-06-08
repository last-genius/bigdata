from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('SimpleSparkProject').getOrCreate()
df = spark.read.csv("PS_20174392719_1491204439457_log.csv")

df.printSchema()
print(f'number of spark rows: {df.count()}')
