#requires pyspark[connect]==3.5.0

import pandas as pd

from pyspark.sql import SparkSession

#SparkSession.builder.master("localhost:7077").getOrCreate().stop()

spark = SparkSession.builder.remote("sc://localhost:15002").getOrCreate()

app_name = "simple-app-pandas"

# Creating a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)
print(df)