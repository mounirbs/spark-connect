# spark-connect
Spark connect provides a local environment for developing Spark applications on Docker. It simulates a Spark cluster and integrates Spark connect to efficiently manage Spark sessions.

## Tested on
Spark 3.5.4, Java 17

## Requirements
- Requires all needed Python packages to be installed in both cluster(workers) and the environment from where the client application is running
- Python versions may need to match in both client and cluster
- No Java is required on the client side
```
pip install -r requirements.txt
```

## Build and Start services (Spark Master, Spark Worker(2x) and Spark Connect)
```
docker compose up -d
```

### Spark Connect tests
```
python ./python/test_spark.py
python ./python/test_pandas.py
python ./python/test_fugue.py
```

## Reference
https://spark.apache.org/docs/latest/spark-connect-overview.html
https://spark.apache.org/docs/latest/api/python/getting_started/quickstart_connect.html
https://spark.apache.org/spark-connect/
