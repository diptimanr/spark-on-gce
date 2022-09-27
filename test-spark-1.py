from pyspark.sql import SparkSession
from datetime import datetime, date

spark = SparkSession.builder.master("local").enableHiveSupport().getOrCreate()

df = spark.createDataFrame([
        (1, 2., 'string1', date(2000, 1, 1), datetime(2000, 1, 1, 12, 0)),
        (2, 3., 'string2', date(2000, 2, 1), datetime(2000, 1, 2, 12, 0)),
        (3, 4., 'string3', date(2000, 3, 1), datetime(2000, 1, 3, 12, 0))
    ], schema='a long, b double, c string, d date, e timestamp')
print("..... Writing data .....")
df.write.mode("overwrite").saveAsTable("test_table_2")
print("..... Complete .....")