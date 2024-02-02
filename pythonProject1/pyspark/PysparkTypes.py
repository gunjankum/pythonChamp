from pyspark.sql import SparkSession

from pyspark.sql.functions import lit, col, instr, expr, pow, round, bround,initcap, translate

spark = SparkSession.builder.appName("TypesPy").getOrCreate()

df = spark.read.option("header", "true") \
    .option("inferSchema", "true") \
    .csv("C:/Users/chand/Videos/Videos/Spark-The-Definitive-Guide-master/data/retail-data/by-day/2010-12-01.csv")

df.show()
df.printSchema()
df.createOrReplaceTempView("dfTable")

df.select(lit(5), lit("five"), lit(5.0)).show()

df.where(col("InvoiceNo") != 536365) \
    .select("InvoiceNo", "Description").show(5, False)

df.where("InvoiceNo = 536365").show(5, False)

# SELECT * FROM dfTable WHERE StockCode in ("DOT") AND(UnitPrice > 600 OR
# instr(Description, "POSTAGE") >= 1)

df.where(col("StockCode").isin("DOT")) \
    .where((col("StockCode") > 600) |
           (instr(col("Description"),
                  "POSTAGE") >= 1)).show()

df.select("CustomerId", expr("pow((Quantity * UnitPrice), 2) + 5")
          .alias("realQuant")).show()


df.select(round(lit(2.5)).alias("ceil"), bround(lit(2.5)).alias("floor")).show()

df.describe().show()

# df.stat.crosstab("StockCode", "Quantity").show()
#
# df.stat.freqItems(["StockCode", "Quantity"]).show()


df.select(initcap(col("Description"))).show(truncate=False)

df.select(translate(col("Description"), "LEET", "1337"), col("Description")).show(2,truncate=False)


df.printSchema()