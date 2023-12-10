from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *



spark = SparkSession.builder.appName("Test1").getOrCreate()

df1 = spark.read.option("header", "true").option("inferSchema", "true").csv(
    "C:/Users/chand/OneDrive/Documents/Spark-The-Definitive-Guide-master/data/flight-data/csv/2010-summary.csv")

# df1.show(10, truncate=False)

# df1.groupBy("DEST_COUNTRY_NAME") \
#     .sum("count") \
#     .withColumnRenamed("sum(count)", "destination_total") \
#     .sort(desc("destination_total")) \
#     .limit(5) \
#     .show()

Myschema = StructType([
    StructField("name",StringType(), True),
    StructField("id",IntegerType(),True)])



data = [("Gunjan",1), ("Kumar",2)]

df2 = spark.createDataFrame(data=data,schema=Myschema)
# df2.show()

df2.selectExpr("count * 2").show()


