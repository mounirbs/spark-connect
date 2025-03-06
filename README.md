# spark-connect
Spark connect provides a local environment for developing Spark applications on Docker. It simulates a Spark cluster and integrates Spark connect to efficiently manage Spark sessions.

## Tested on
Spark 3.5.4, Python 3.10, Java 17

## Requirements
- Requires all needed Python packages to be installed in both cluster(workers) and the environment from where the client application is running
- Python versions needs to match in both client and cluster, since the driver runs in the client side when using pyspark(only client mode is supported)
- No Java is required on the client side
```
pip install -r requirements.txt
```

## Build and Start services (Spark Master, Spark Worker, and Spark Connect)
```
docker compose up -d --build
```

### Spark Connect tests
```
kubectl -n spark-connect port-forward svc/spark-connect 15002:15002
python ./python/test_spark.py
python ./python/test_pandas.py
python ./python/test_fugue.py
```
## Convert docker-compose to Helm chart
```
kompose --file docker-compose.yml convert -o helm -c
```
Some adjustments/cleaning were done on the helm chart created by kompose.

## Helm
```
helm package helm/spark-connect -d helm/

kubectl create namespace spark-connect

helm install -n spark-connect spark-connect helm/spark-connect-0.0.1.tgz

kubectl -n spark-connect get all

helm uninstall spark-connect -n spark-connect
```

## Reference
https://spark.apache.org/docs/latest/spark-connect-overview.html
https://spark.apache.org/docs/latest/api/python/getting_started/quickstart_connect.html
https://spark.apache.org/spark-connect/
