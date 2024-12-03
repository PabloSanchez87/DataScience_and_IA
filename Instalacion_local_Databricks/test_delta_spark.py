from pyspark.sql import SparkSession
from delta import configure_spark_with_delta_pip

builder = SparkSession.builder \
    .appName("PruebaDelta") \
    .config("spark.master", "local[*]") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")

spark = configure_spark_with_delta_pip(builder).getOrCreate()

# Crear un DataFrame y guardarlo como Delta
data = [(1, "Alice"), (2, "Bob"), (3, "Cathy")]
df = spark.createDataFrame(data, ["id", "name"])
df.write.format("delta").mode("overwrite").save("delta_table")

# Leer la tabla Delta
delta_df = spark.read.format("delta").load("delta_table")
delta_df.show()
