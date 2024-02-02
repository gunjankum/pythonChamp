from pyspark.sql import SparkSession

from pyspark.sql.functions import col, column, expr, avg, count, lit

spark = SparkSession.builder.appName("MyPysparkFuncs").config("spark.log.level", "INFO").getOrCreate()

df = spark.read.option("inferSchema",
                       "true").option("header", "true") \
    .json("C:/Users/chand/Videos/Videos/Spark-The-Definitive-Guide-master/"
          "data/flight-data/json/2015-summary.json")

# df.select(col("count"), col("DEST_COUNTRY_NAME")).show(truncate=False)

# x = df.first()
# print(x)

# df.select("DEST_COUNTRY_NAME", "count").show()

df.select(col("DEST_COUNTRY_NAME"), column("DEST_COUNTRY_NAME"), expr("DEST_COUNTRY_NAME")).show(2)

df.selectExpr("DEST_COUNTRY_NAME as destination", "DEST_COUNTRY_NAME").show(2)

df.selectExpr("*", "(DEST_COUNTRY_NAME = ORIGIN_COUNTRY_NAME) as withinCountry").show(2)

df.select("*").show(5)

df.selectExpr("avg(count) as average", "count(distinct (DEST_COUNTRY_NAME)) as count").show(2)

df.select(expr("*"), lit(1).alias("One")).show(2)

df.select("DEST_COUNTRY_NAME", lit(2).alias("Two")).show(2)

# Add Columns

df.withColumn("numberOne", lit(2)).show(2)

df.withColumn("withinCountry", expr("DEST_COUNTRY_NAME == ORIGIN_COUNTRY_NAME")).show(2)

# Rename col

# df.withColumn("Destination", expr("DEST_COUNTRY_NAME"))

# Rename Col

df.withColumnRenamed("DEST_COUNTRY_NAME", "dest").show(2)

dfWithLongColName = df.withColumn("This is s long column", expr("ORIGIN_COUNTRY_NAME"))

# SELECT `This Long Column-Name`, `This Long Column-Name` as `new col`
# FROM dfTableLong LIMIT 2
dfWithLongColName.selectExpr("`This is s long column`", "`This is s long column` as `new col`").show(2)

dfWithLongColName.select("This is s long column").show(3)

dfWithLongColName.show(1)

dfWithLongColName.drop("DEST_COUNTRY_NAME")
dfWithLongColName.show(2)

# Cast columns

df.withColumn("count2", col("count").cast("long"))

# Count

# df.filter(col("count") < 2).show(2)

df.where("count < 5 ").show(5)

df.where(col("count") < 2).where(col("DEST_COUNTRY_NAME") != "Croatia").show(6)

# distinct

count = df.select("DEST_COUNTRY_NAME", "ORIGIN_COUNTRY_NAME").distinct().count()
print(count)

# sample DF
seed = 5
withReplacement = False
fraction = 0.5

samp = df.sample(withReplacement, fraction, seed).count()

print(samp)
