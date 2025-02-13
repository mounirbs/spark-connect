from pyspark.sql import SparkSession

#SparkSession.builder.master("localhost:7077").getOrCreate().stop()

spark = SparkSession.builder.remote("sc://localhost:15002").appName("SimpleAppSparkDF").getOrCreate()

# Read CSV File (the data needs to be accessible from the Spark-Connect server, and the workers)
df = spark.read.csv("/data/test.csv", header=True, inferSchema=True)
df.show()

df.createOrReplaceTempView("capitals")

spark.sql("select Continent, count(*) as Total from capitals group by Continent order by Total desc").show()

spark.stop()
