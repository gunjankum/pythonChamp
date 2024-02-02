from pyspark.sql import SparkSession

from pyspark.sql import Row

from pyspark.sql.functions import col, column, expr, avg, count, lit, asc, desc

spark = SparkSession.builder.appName("MyPysparkFuncs").config("spark.log.level", "INFO").getOrCreate()

df = spark.read.option("inferSchema",
                       "true").option("header", "true") \
    .json("C:/Users/chand/Videos/Videos/Spark-The-Definitive-Guide-master/"
          "data/flight-data/json/2015-summary.json")

# # union
#
# schema = df.schema
# newRows = [
#     Row("New Country", "Other Country", 5),
#     Row("New Country 2", "Other Country 3", 1)
# ]
# parallelizedRows = spark.sparkContext.parallelize(newRows)
# newDF = spark.createDataFrame(parallelizedRows, schema)
# # in Python
# df.union(newDF) \
#     .where("count = 1") \
#     .where(col("ORIGIN_COUNTRY_NAME") != "United States") \
#     .show()


df.sort("count").show()

df.orderBy("count", "DEST_COUNTRY_NAME").show(5)


df.orderBy(expr("count desc"), expr("DEST_COUNTRY_NAME asc")).show()



# Repartition and Coalesce


num = df.rdd.getNumPartitions()
print(num)

df.repartition(10)

num2 = df.rdd.getNumPartitions()
print(num2)

df.repartition(col("DEST_COUNTRY_NAME"))
df.repartition(5, col("DEST_COUNTRY_NAME"))

df.repartition(5, col("DEST_COUNTRY_NAME")).coalesce(2)






