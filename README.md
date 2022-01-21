# Spark and Delta Lake

## Setup

[Download](https://spark.apache.org/downloads.html) and extract Spark.

Start a Spark cluster in [stand-alone mode](https://spark.apache.org/docs/latest/spark-standalone.html) and navigate to [`http://localhost:8080`](http://localhost:8080).

Spark cluster listens on port 7077 by default.

## Install dependencies

```bash
$ pip install -e .
```

Follow the [instructions](https://docs.delta.io/latest/quick-start.html) how to start with Delta Lake:

```bash
$ pyspark --packages io.delta:delta-core_2.12:1.1.0 --conf "spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension" --conf "spark.sql.catalog.spark_catalog=org.apache.spark.sql.delta.catalog.DeltaCatalog"
```