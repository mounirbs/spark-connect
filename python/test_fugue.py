import os
os.environ["PYARROW_IGNORE_TIMEZONE"]="1"

from pyspark.sql import SparkSession

spark = SparkSession.builder.remote("sc://localhost:15002").appName("SimpleAppPandas").getOrCreate()

import pandas as pd
from typing import Dict

input_df = pd.DataFrame({"id":[0,1,2], "value": (["A", "B", "C"])})
map_dict = {"A": "Apple", "B": "Banana", "C": "Carrot"}

def map_letter_to_food(df: pd.DataFrame, mapping: Dict[str, str]) -> pd.DataFrame:
    df["value"] = df["value"].map(mapping)
    return df

from fugue import transform
sdf = spark.createDataFrame(input_df)

out = transform(sdf,
               map_letter_to_food,
               schema="*",
               params=dict(mapping=map_dict),
               )
# out is a Spark DataFrame
out.show()

spark.stop()
