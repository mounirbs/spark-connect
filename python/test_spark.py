#requires pyspark[connect]==3.5.0

from pyspark.sql import SparkSession

#SparkSession.builder.master("localhost:7077").getOrCreate().stop()

spark = SparkSession.builder.remote("sc://localhost:15002").getOrCreate()

df = spark.createDataFrame([{"id": 1, "name": "Mounir-SparkConnect"}])

df.show()