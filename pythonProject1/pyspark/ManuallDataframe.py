from pyspark.sql import SparkSession
from pyspark.sql.types import StructField, StructType, StringType, LongType
from pyspark.sql import Row

spark = SparkSession.builder.appName("ManualDF").getOrCreate()

myManualSchema = StructType([
    StructField("some", StringType(), True),
    StructField("col", StringType(), True),
    StructField("names", LongType(), False)
])
myRow = Row("Hello", "None", 1)
myDf = spark.createDataFrame([myRow], myManualSchema)
myDf.show()
