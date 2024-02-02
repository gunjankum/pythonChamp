from pyspark.sql import SparkSession
from pyspark.sql.functions import first, last, desc, sumDistinct, to_date, max
from pyspark.sql.window import Window


spark = SparkSession \
    .builder \
    .appName("PyAgg") \
    .getOrCreate()

df = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .csv("C:/Users/chand/OneDrive/Documents/Spark-The-Definitive-Guide-master/data/retail-data/by-day/2010-12-01.csv")


df.show()
# df.select(first("StockCode"), last("StockCode")).show(truncate=False)
# df.select(sumDistinct("Quantity")).show(truncate=False)


# df.groupby("InvoiceNo", "CustomerID").count().show()

df.withColumn("date", to_date("InvoiceDate","MM/d/yyyy H:mm")).show()

windowSpec = Window.partitionBy("CustomerID", "date")\
              .orderBy(desc("Quantity"))\
              .rowsBetween(Window.unboundedPreceding, Window.currentRow)

maxPurchaseQuantity = max("Quantity").over(windowSpec)


