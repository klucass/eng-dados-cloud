from pyspark.sql.functions import mean, max, min, col, count
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Spark").getOrCreate()

# Ler os dados do Enem 2019
enem = (
    spark
    .read
    .format("csv")
    .option("header", True)
    .option("inferSchema", True )
    .option("delimiter", ";")
    .load("s3://datalake-kennedylucas-igti/enem2019/raw/")
)

(
    enem
    .write
    .mode("overwrite")
    .format("parquet")
    .partitionBy("year")
    .save("s3://datalake-kennedylucas-igti/enem2019/consumer-zone/")
)