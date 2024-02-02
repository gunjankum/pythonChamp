from pyspark.sql import SparkSession
from pyspark.sql.functions import max, desc

spark = SparkSession.builder.appName("MyPyspark").config("spark.log.level", "INFO").getOrCreate()

flightData = spark.read.option("inferSchema", "true").option("header", "true").csv(
    "C:/Users/chand/Videos/Videos/Spark-The-Definitive-Guide-master/data/flight-data/csv/2015-summary.csv")

# flightData.printSchema()
# flightData.show(truncate=False)

# flightData.sort("count").explain()

spark.conf.set("spark.sql.shuffle.partitions", "5")

# flightData.sort("count").take(2)
#
# max_count = flightData.select(max("count")).take(1)
# print(max_count)

# flightData \
#     .groupBy("DEST_COUNTRY_NAME") \
#     .sum("count") \
#     .withColumnRenamed("sum(count)", "destination_total") \
#     .sort(desc("destination_total")) \
#     .limit(5) \
#     .show()


spark.read.json("C:/Users/chand/Videos/Videos/Spark-The-Definitive-Guide-master/data/flight-data/json/2015-summary.json").schema
