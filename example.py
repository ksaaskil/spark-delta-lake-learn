import logging
from pathlib import Path
import uuid

from delta import DeltaTable, configure_spark_with_delta_pip
import pyspark
from pyspark.sql.functions import expr


def build():
    builder = (
        pyspark.sql.SparkSession.builder.appName("MyApp")
        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
        .config(
            "spark.sql.catalog.spark_catalog",
            "org.apache.spark.sql.delta.catalog.DeltaCatalog",
        )
    )

    spark = configure_spark_with_delta_pip(builder).getOrCreate()
    return spark


DELTA_TABLE_DIR = str(Path("./delta-table").joinpath(str(uuid.uuid4())[:8]))


def main():
    logging.basicConfig(level=logging.INFO)
    spark = build()

    data = spark.range(0, 5)

    logging.info(f"Writing DF to {DELTA_TABLE_DIR}")
    data.write.format("delta").save(DELTA_TABLE_DIR)

    logging.info(f"Reading from {DELTA_TABLE_DIR}")
    df = spark.read.format("delta").load(DELTA_TABLE_DIR)
    df.show()

    data = spark.range(5, 10)
    logging.info(f"Overwriting with new values to {DELTA_TABLE_DIR}")
    data.write.format("delta").mode("overwrite").save(DELTA_TABLE_DIR)

    logging.info("Creating an instance of DeltaTable, updating values with condition")
    delta_table = DeltaTable.forPath(spark, DELTA_TABLE_DIR)
    delta_table.update(condition=expr("id % 2 == 0"), set={"id": expr("id + 100")})
    delta_table.toDF().show()

    logging.info("Reading version 0 before overwrite")
    df = spark.read.format("delta").option("versionAsOf", 0).load(DELTA_TABLE_DIR)
    df.show()


if __name__ == "__main__":
    main()
