from pyspark.sql.types import StructField, StructType, StringType, LongType
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("MyPysparkSchema").config("spark.log.level", "INFO").getOrCreate()

MySchema = StructType([StructField("DEST_COUNTRY_NAME", StringType(), True),
                       StructField("ORIGIN_COUNTRY_NAME", StringType(), True),
                       StructField("count", LongType(), False, metadata={"hello": "world"})])

df = spark.read.schema(MySchema) \
    .json("C:/Users/chand/Videos/Videos/Spark-The-Definitive-Guide-master/"
          "data/flight-data/json/2015-summary.json")

df.printSchema()
