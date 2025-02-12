#requires pyspark[connect]==3.5.0
import os
os.environ["PYARROW_IGNORE_TIMEZONE"]="1"

import pyspark.pandas as ps

from pyspark.sql import SparkSession

#SparkSession.builder.master("localhost:7077").getOrCreate().stop()

spark = SparkSession.builder.remote("sc://localhost:15002").appName("SimpleAppPandasOnSpark").getOrCreate()

# Creating a DataFrame from a dictionary
data = {
    'name': ['Pandas', 'On', 'Spark'],
    'key': [1, 2, 3],
    'value': ['asdnaP', 'nO', 'krapS']
}

df = ps.DataFrame(data)
print(df)

spark.stop()
