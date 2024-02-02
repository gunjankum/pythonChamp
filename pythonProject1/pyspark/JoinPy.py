from pyspark.sql import SparkSession, Row

# Create a SparkSession
spark = SparkSession.builder.appName("LeftJoinExample").getOrCreate()

# Sample DataFrames with Row objects
data1 = [Row(id=1, name="Alice"), Row(id=2, name="Bob"), Row(id=3, name="Charlie")]
data2 = [Row(id=1, subject="Math"), Row(id=3, subject="Science"), Row(id=4, subject="History")]

df1 = spark.createDataFrame(data1)
df2 = spark.createDataFrame(data2)

# Perform a left join
left_join_result = df1.join(df2, on="id", how="left")

# Show the result
left_join_result.show()
