'''
Necesario instalar JAVA

# Linux
sudo apt update
sudo apt install openjdk-11-jdk


'''


from pyspark.sql import SparkSession

# Crear una sesión de Spark
spark = SparkSession.builder \
    .appName("PruebaLocal") \
    .config("spark.master", "local[*]") \
    .getOrCreate()

# Verificar la versión de Spark
print("Versión de Spark:", spark.version)

# Crear un DataFrame simple
data = [(1, "Alice"), (2, "Bob"), (3, "Cathy")]
df = spark.createDataFrame(data, ["id", "name"])
df.show()
