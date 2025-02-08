#requires pyspark[connect]==3.5.0
import os
os.environ["PYARROW_IGNORE_TIMEZONE"]="1"

import pyspark.pandas as ps

from pyspark.sql import SparkSession

#SparkSession.builder.master("localhost:7077").getOrCreate().stop()

spark = SparkSession.builder.remote("sc://localhost:15002").appName("SimpleAppPandas").getOrCreate()

# Creating a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = ps.DataFrame(data)
print(df)

spark.stop()
