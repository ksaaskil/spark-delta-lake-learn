# Spark and Delta Lake

## Setup

[Download](https://spark.apache.org/downloads.html) and extract Spark.

Start a Spark cluster in [stand-alone mode](https://spark.apache.org/docs/latest/spark-standalone.html) and navigate to [`http://localhost:8080`](http://localhost:8080). Spark cluster listens on port 7077 by default.

For example, start a master and worker as follows:

```bash
$ ~/Libraries/spark-3.2.0-bin-hadoop3.2/sbin/start-master.sh
$ ~/Libraries/spark-3.2.0-bin-hadoop3.2/sbin/start-worker.sh spark://Kimmos-MBP.localdomain:7077
```

Replace the Spark URL for your installation.

Start a Spark shell, for example:

```bash
$ ~/Libraries/spark-3.2.0-bin-hadoop3.2/bin/spark-shell --master spark://Kimmos-MBP.localdomain:7077
```

## Install dependencies

```bash
$ pip install -e .
```

Run `python example.py`.

Follow the [instructions](https://docs.delta.io/latest/quick-start.html) how to start `pyspark` with Delta Lake dependencies:

```bash
$ pyspark --packages io.delta:delta-core_2.12:1.1.0 --conf "spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension" --conf "spark.sql.catalog.spark_catalog=org.apache.spark.sql.delta.catalog.DeltaCatalog"
```
