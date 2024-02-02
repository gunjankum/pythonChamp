from pyspark.sql import SparkSession

from pyspark.sql.functions import current_date, current_timestamp, date_add,date_sub,coalesce, split, array_contains
spark = SparkSession.builder.appName("DatesPy").getOrCreate()

df = spark.read.option("header", "true") \
    .option("inferSchema", "true") \
    .csv("C:/Users/chand/Videos/Videos/Spark-The-Definitive-Guide-master/data/retail-data/by-day/2010-12-01.csv")

dateDF = spark.range(10).withColumn("Date", current_date()).withColumn("time", current_timestamp())

dateDF.createOrReplaceTempView("dateTable")
dateDF.printSchema()

dateDF.select(date_add("Date", 5), date_sub("Date", 5)).show()

df.select(coalesce("Description", "CustomerId")).show(truncate=False)

df.na.drop("any")
df.na.drop("all")
df.na.fill("Hi")
df.na.fill("all", subset=["StockCode"])


df.select(split("Description", " ")
          .alias("split_desc"))\
    .selectExpr("split_desc[0]").show()

df.select(array_contains(split("Description", " "),"WHITE")).show()






