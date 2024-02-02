from pyspark.sql import SparkSession

from pyspark.sql.functions import udf,col

spark = SparkSession \
    .builder \
    .appName("PyUDF") \
    .getOrCreate()

df = spark.range(10).toDF("num")


def pow3(triple):
    return triple ** 3


res = pow3(2)
print(res)

pow3 = udf(pow3)

df.select(pow3(col("num"))).show()
