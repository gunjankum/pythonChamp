from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

spark = SparkSession.builder.appName("Test1").getOrCreate()

# df1 = spark.read.option("header", "true").option("inferSchema", "true").csv(
#     "C:/Users/chand/OneDrive/Documents/Spark-The-Definitive-Guide-master/data/flight-data/csv/2010-summary.csv")

# df1.show(10, truncate=False)

# df1.groupBy("DEST_COUNTRY_NAME") \
#     .sum("count") \
#     .withColumnRenamed("sum(count)", "destination_total") \
#     .sort(desc("destination_total")) \
#     .limit(5) \
#     .show()

# Myschema = StructType([
#     StructField("name", StringType(), True),
#     StructField("id", IntegerType(), True)])
#
# data = [("Gunjan", 1), ("Kumar", 2)]

# df2 = spark.createDataFrame(data=data, schema=Myschema)
# df2.show()

# df1.selectExpr("*", "(DEST_COUNTRY_NAME = ORIGIN_COUNTRY_NAME) as withinCountry").show(2)

# df1.selectExpr("count * 3").show()
# df1.selectExpr("avg(count)", "count(distinct(DEST_COUNTRY_NAME))").show()
#
# df1.select(expr("*"), lit(1).alias("one")).show()

# df1.select("*", lit(1).alias("One")).show()

# df1.withColumn("One", lit(1)).show()
#
# df1.withColumn("NewCount", expr("count * 5")).show()


# df1.where("count > 100").where(col("DEST_COUNTRY_NAME") == "Ireland").show()
#
# df1.groupBy("DEST_COUNTRY_NAME").count(count).show()


# raw = [("Gunjan", "30", "Bangalore")]

# df_raw = spark.createDataFrame(raw).toDF("name","age","place")
# df_raw.show()
# df_raw.printSchema()
#
# df_raw.select("name").show()
# df_raw.select("*").show()


# data_new = [(100,200,3),(200,4,5),(300,5,4)]
# df4 =  spark.createDataFrame(data_new).toDF("col1","col2","col3")
# # df4.select(df4.col1 + df4.col2).show()
# df4.select(df4.col1 * 2).show()
# df4.select(df4.)


# data = [("James", "Bond", "100", None),
#         ("Ann", "Varsa", "200", 'F'),
#         ("Tom Cruise", "XXX", "400", ''),
#         ("Tom Brand", None, "400", 'M')]
# columns = ["fname", "lname", "id", "gender"]
# df = spark.createDataFrame(data, columns)


# df.select(df.fname.alias("first_name"),df.lname.alias("last_name")).show()
# df.sort(df.fname.desc()).show()
# df.printSchema()
#
# df.select(df.id.cast("int")).printSchema()

# df.filter(df.fname.contains("James")).show()
# df.filter((df.id.between(100,300))).show()
# df.filter(df.fname.startswith("T")).show()
# df.filter(df.lname.endswith("d")).show()

# df.filter(df.lname.isNull()).show()
# df.filter(df.lname.isNotNull()).show()

# df.select(df.fname).filter(df.fname.like("%am%")).show()
# df.select(df.fname.substr(1,2).alias("Sub")).show()


# df.select(df.fname,df.lname,when(df.gender=='M',"Male")
#           .when(df.gender=="F","Female")
#           .when(df.gender==None,"")
#           .otherwise(df.gender).alias("others")).show()

# df.withColumn("First",df.fname).show()


# data1 = [('James', '', 'Smith', '1991-04-01', 'M', 3000),
#          ('Michael', 'Rose', '', '2000-05-19', 'M', 4000),
#          ('Robert', '', 'Williams', '1978-09-05', 'M', 4000),
#          ('Maria', 'Anne', 'Jones', '1967-12-01', 'F', 4000),
#          ('Jen', 'Mary', 'Brown', '1980-02-17', 'F', -1)
#          ]
#
# columns = ["firstname", "middlename", "lastname", "dob", "gender", "salary"]
#
# df5 = spark.createDataFrame(data=data1, schema=columns)
# df5.printSchema()
#
# df5.withColumn('salary',df5.salary.cast('Integer')).printSchema()
#
# df5.withColumn("Country",lit("USA")).show()
#
# df5.withColumn("salary",df5.salary * 5).show()

# df5.withColumn("High_Salary", df5.salary * 10).show()
#
# #
#
# df5.withColumnRenamed("gender","sex").show()

# df5.drop("salary").show()

# dataDF = [(('James', '', 'Smith'), '1991-04-01', 'M', 3000),
#           (('Michael', 'Rose', ''), '2000-05-19', 'M', 4000),
#           (('Robert', '', 'Williams'), '1978-09-05', 'M', 4000),
#           (('Maria', 'Anne', 'Jones'), '1967-12-01', 'F', 4000),
#           (('Jen', 'Mary', 'Brown'), '1980-02-17', 'F', -1)
#           ]

# schema = StructType([
#     StructField('name', StructType([
#         StructField('firstname', StringType(), True),
#         StructField('middlename', StringType(), True),
#         StructField('lastname', StringType(), True)
#     ])),
#     StructField('dob', StringType(), True),
#     StructField('gender', StringType(), True),
#     StructField('salary', IntegerType(), True)
# ])
#
# df6 = spark.createDataFrame(data=dataDF, schema=schema)
#
# df6.printSchema()
#
# df6.withColumnRenamed("dob", "date_of_birth").withColumnRenamed("salary","Comp").show()
#
# df6.withColumn("DateOfBirth",df6.dob).show()

# data2 = [
#     (("James", "", "Smith"), ["Java", "Scala", "C++"], "OH", "M"),
#     (("Anna", "Rose", ""), ["Spark", "Java", "C++"], "NY", "F"),
#     (("Julia", "", "Williams"), ["CSharp", "VB"], "OH", "F"),
#     (("Maria", "Anne", "Jones"), ["CSharp", "VB"], "NY", "M"),
#     (("Jen", "Mary", "Brown"), ["CSharp", "VB"], "NY", "M"),
#     (("Mike", "Mary", "Williams"), ["Python", "VB"], "OH", "M")
# ]
#
# schema2 = StructType([
#     StructField('name', StructType([
#         StructField('firstname', StringType(), True),
#         StructField('middlename', StringType(), True),
#         StructField('lastname', StringType(), True)
#     ])),
#     StructField('languages', ArrayType(StringType()), True),
#     StructField('state', StringType(), True),
#     StructField('gender', StringType(), True)
# ])
#
# df7 = spark.createDataFrame(data=data2, schema=schema2)
# df7.printSchema()


# df7.filter(df7.state != "OH").show()
# df7.filter("state == 'OH'").show()

# df7.filter((df7.state == "OH") & (df7.gender == "F")).show()
#
# df7.select(df7.name.firstname.substr(1, 2)).show()


# data = [("James", "Sales", 3000), ("Michael", "Sales", 4600), ("Robert", "Sales", 4100), ("Maria", "Finance", 3000),
#         ("James", "Sales", 3000), ("Scott", "Finance", 3300), ("Jen", "Finance", 3900), ("Jeff", "Marketing", 3000),
#         ("Kumar", "Marketing", 2000), ("Saif", "Sales", 4100)]
#
# # Create DataFrame
# columns = ["employee_name", "department", "salary"]
# df = spark.createDataFrame(data=data, schema=columns)
# df.printSchema()
# df.show(truncate=False)

# num = df.count()
#
# print(num)
#
# num1 = df.distinct().count()
# print(num1)

# df.drop_duplicates().show()

# df.distinct().show()

# simpleData = [("James", "Sales", "NY", 90000, 34, 10000),
#               ("Michael", "Sales", "NY", 86000, 56, 20000),
#               ("Robert", "Sales", "CA", 81000, 30, 23000),
#               ("Maria", "Finance", "CA", 90000, 24, 23000),
#               ("Raman", "Finance", "CA", 99000, 40, 24000),
#               ("Scott", "Finance", "NY", 83000, 36, 19000),
#               ("Jen", "Finance", "NY", 79000, 53, 15000),
#               ("Jeff", "Marketing", "CA", 80000, 25, 18000),
#               ("Kumar", "Marketing", "NY", 91000, 50, 21000)
#               ]
# columns = ["employee_name", "department", "state", "salary", "age", "bonus"]
# df = spark.createDataFrame(data=simpleData, schema=columns)

# df.sort("department", "state").show()
#
# df.orderBy("department", "state").show()


# df.sort(df.department.asc(), df.state.desc()).show()
# df.orderBy(df.department.asc(), df.state.asc()).show()


# simpleData = [("James", "Sales", "NY", 90000, 34, 10000),
#               ("Michael", "Sales", "NY", 86000, 56, 20000),
#               ("Robert", "Sales", "CA", 81000, 30, 23000),
#               ("Maria", "Finance", "CA", 90000, 24, 23000),
#               ("Raman", "Finance", "CA", 99000, 40, 24000),
#               ("Scott", "Finance", "NY", 83000, 36, 19000),
#               ("Jen", "Finance", "NY", 79000, 53, 15000),
#               ("Jeff", "Marketing", "CA", 80000, 25, 18000),
#               ("Kumar", "Marketing", "NY", 91000, 50, 21000)
#               ]
#
# schema = ["employee_name", "department", "state", "salary", "age", "bonus"]
# df = spark.createDataFrame(data=simpleData, schema=schema)
# df.printSchema()

# df.groupBy("department").sum("salary").show()
#
# df.groupBy("department").min("salary").show()
#
# df.groupBy("department", "state").sum("salary", "bonus").show()

# df.groupBy("department").agg(sum(df.salary.alias("Comp")).where(col("Comp") > 200000).show()
#
# df.groupBy("department") \
#     .agg(sum("salary").alias("sum_salary"),
#          avg("salary").alias("avg_salary"),
#          sum("bonus").alias("sum_bonus"),
#          max("bonus").alias("max_bonus")).where(col("sum_bonus") >= 50000) .show(truncate=False)

# emp = [(1, "Smith", -1, "2018", "10", "M", 3000), \
#        (2, "Rose", 1, "2010", "20", "M", 4000), \
#        (3, "Williams", 1, "2010", "10", "M", 1000), \
#        (4, "Jones", 2, "2005", "10", "F", 2000), \
#        (5, "Brown", 2, "2010", "40", "", -1), \
#        (6, "Brown", 2, "2010", "50", "", -1) \
#        ]
# empColumns = ["emp_id", "name", "superior_emp_id", "year_joined", \
#               "emp_dept_id", "gender", "salary"]
#
# empDF = spark.createDataFrame(data=emp, schema=empColumns)
# empDF.printSchema()
# # empDF.show(truncate=False)
#
# dept = [("Finance", 10),
#         ("Marketing", 20),
#         ("Sales", 30),
#         ("IT", 40)
#         ]
# deptColumns = ["dept_name", "dept_id"]
# deptDF = spark.createDataFrame(data=dept, schema=deptColumns)
# deptDF.printSchema()
# # deptDF.show(truncate=False)
#
# empDF.join(deptDF,empDF.emp_dept_id==deptDF.dept_id,"inner").show()
#
# empDF.join(deptDF,empDF.emp_dept_id==deptDF.dept_id,"outer").show()

# empDF.join(deptDF,empDF.emp_dept_id==deptDF.dept_id,"full").show()
#
# empDF.join(deptDF,empDF.emp_dept_id==deptDF.dept_id,"fullouter").show()

# empDF.join(deptDF,empDF.emp_dept_id==deptDF.dept_id,"left").show()
#
# # empDF.join(deptDF,empDF.emp_dept_id==deptDF.dept_id,"right").show()
#
# empDF.join(deptDF,empDF.emp_dept_id==deptDF.dept_id,"leftsemi").show()
#
# empDF.join(deptDF,empDF.emp_dept_id==deptDF.dept_id,"leftanti").show()

# simpleData = [("James","Sales","NY",90000,34,10000), \
#     ("Michael","Sales","NY",86000,56,20000), \
#     ("Robert","Sales","CA",81000,30,23000), \
#     ("Maria","Finance","CA",90000,24,23000) \
#   ]
#
# columns= ["employee_name","department","state","salary","age","bonus"]
# df = spark.createDataFrame(data = simpleData, schema = columns)
# df.printSchema()
# df.show(truncate=False)
#
# simpleData2 = [("James","Sales","NY",90000,34,10000), \
#     ("Maria","Finance","CA",90000,24,23000), \
#     ("Jen","Finance","NY",79000,53,15000), \
#     ("Jeff","Marketing","CA",80000,25,18000), \
#     ("Kumar","Marketing","NY",91000,50,21000) \
#   ]
# columns2= ["employee_name","department","state","salary","age","bonus"]
#
# df2 = spark.createDataFrame(data = simpleData2, schema = columns2)
#
# df2.printSchema()
# df2.show(truncate=False)
#
# df.union(df2).show()
#
# df.union(df2).distinct().show(truncate=False)


# data = [
#  ("James,,Smith",["Java","Scala","C++"],["Spark","Java"]),
#  ("Michael,Rose,",["Spark","Java","C++"],["Spark","Java"]),
#  ("Robert,,Williams",["CSharp","VB"],["Spark","Python"])
# ]
# df = spark.createDataFrame(data=data,schema=["Name","Languages1","Languages2"])
# df.printSchema()
# df.show()
#
# df.select(transform("Languages1", lambda x: upper(x).alias("NewLang"))).show()


# Prepare Data
# columns = ["Seqno", "Name"]
# data = [("1", "john jones"),
#         ("2", "tracey smith"),
#         ("3", "amy sanders")]
#
# # Create DataFrame
# df = spark.createDataFrame(data=data, schema=columns)
# df.show()
#
#
#
#
# accum = spark.sparkContext.accumulator(0)
# df.foreach(lambda x : accum.add(int(x.Seqno)))
# print(accum.value)

# filepath  = "C:/Users/chand/Downloads/small_zipcode.csv"
# df = spark.read.options(header="true",inferSchema='true').csv(filepath)
# df.show()
#
# df.na.fill(0).show()
# df.na.fill(0,["population"]).show()
#
#
# df.na.fill("unknown", ["city"]).na.fill("",["type"]).show()


# data = [
#     ("James",None,"M"),
#     ("Anna","NY","F"),
#     ("Julia",None,None)
#   ]
#
# columns = ["name","state","gender"]
# df = spark.createDataFrame(data,columns)
# df.show()
#
# df.filter("state is  null").show()
# df.filter("state is not null").show()
# df.filter(df.state.isNull() & df.gender.isNull()).show()


# Create spark session

# data = [("Banana",1000,"USA"), ("Carrots",1500,"USA"), ("Beans",1600,"USA"), \
#       ("Orange",2000,"USA"),("Orange",2000,"USA"),("Banana",400,"China"), \
#       ("Carrots",1200,"China"),("Beans",1500,"China"),("Orange",4000,"China"), \
#       ("Banana",2000,"Canada"),("Carrots",2000,"Canada"),("Beans",2000,"Mexico")]
#
# columns= ["Product","Amount","Country"]
# df = spark.createDataFrame(data = data, schema = columns)
# df.printSchema()
# df.show(truncate=False)
#
#
# pivot_df = df.groupby("Product").pivot("Country").sum("Amount")
# pivot_df.printSchema()
# pivot_df.show()
#
# df.groupby("Country","Product").sum("Amount").show()

# df = spark.read.options(header="true",inferSchema='true').csv("C:/Users/chand/Downloads/simple-zipcodes.csv")
# df.printSchema()
# df.show()
# df.write.options(header="true").partitionBy("state").mode("overWrite").csv("C:/Users/chand/Downloads/zipcodes-state")
# df.write.options(header="true").partitionBy("state","city").mode("overWrite").csv("C:/Users/chand/Downloads/zipcodes-state")

# df.repartition(2)\
#     .write\
#     .options(header="true")\
#     .partitionBy("state")\
#     .mode("overWrite")\
#     .csv("C:/Users/chand/Downloads/zipcodes-state")

# df.write\
#     .options(header="true")\
#     .options(maxRecordsPerFile=2)\
#     .partitionBy("state")\
#     .mode("overWrite")\
#     .csv("C:/Users/chand/Downloads/zipcodes-state")


# simpleData = [("James", "Sales", 3000),
#               ("Michael", "Sales", 4600),
#               ("Robert", "Sales", 4100),
#               ("Maria", "Finance", 3000),
#               ("James", "Sales", 3000),
#               ("Scott", "Finance", 3300),
#               ("Jen", "Finance", 3900),
#               ("Jeff", "Marketing", 3000),
#               ("Kumar", "Marketing", 2000),
#               ("Saif", "Sales", 4100)
#               ]
# schema = ["employee_name", "department", "salary"]
# df = spark.createDataFrame(data=simpleData, schema=schema)
# df.printSchema()
# df.show(truncate=False)

# avg = df.select(avg("salary"))
# avg.show()
#
# df.select(count("employee_name")).show()

# df.groupBy("department").agg(sum(df.salary).alias("Sum_Salary")).show()
# df.select(first("salary")).show()
#
# df.select(last("salary")).show()
#
# df.select(collect_list("salary")).show(truncate=False)
# df.select(collect_set("salary")).show(truncate=False)
#
# df.select(countDistinct("department")).show()
# df.select(count("department")).show()
#
# df.select(sum("salary")).show()
# df.select(sumDistinct("salary")).show()

# Window

from pyspark.sql.window import *

# simpleData = (("James", "Sales", 3000),
#               ("Michael", "Sales", 4600),
#               ("Robert", "Sales", 4100),
#               ("Maria", "Finance", 3000),
#               ("James", "Sales", 3000),
#               ("Scott", "Finance", 3300),
#               ("Jen", "Finance", 3900),
#               ("Jeff", "Marketing", 3000),
#               ("Kumar", "Marketing", 2000),
#               ("Saif", "Sales", 4100)
#               )
#
# columns = ["employee_name", "department", "salary"]
# df = spark.createDataFrame(data=simpleData, schema=columns)
# df.printSchema()
# df.show(truncate=False)
#

# df.groupby("department")\
#     .agg(avg("salary")\
#     .alias("avg"),sum("salary")\
#     .alias("sum"),min("salary")\
#     .alias("min"),max("salary")\
#     .alias("max")).show(truncate=False)

# w = Window.partitionBy("department").orderBy("salary")

#
# df.show()
# # df.withColumn("rowNum",row_number().over(w)).show(truncate=False)
# # df.withColumn("rank",rank().over(w)).show(truncate=False)
# # df.withColumn("lead",lead("salary",1).over(w)).show()
# df.withColumn("lead",lag("salary",1).over(w)).show()





# # Sample e-commerce order data
# data = [
#     (1, "CustomerA", "2023-09-15 10:00:00", "2023-09-15 10:30:00"),
#     (2, "CustomerA", "2023-09-15 11:00:00", "2023-09-15 11:15:00"),
#     (3, "CustomerA", "2023-09-15 12:00:00", "2023-09-15 12:30:00"),
#     (4, "CustomerB", "2023-09-15 10:30:00", "2023-09-15 11:00:00"),
#     (5, "CustomerB", "2023-09-15 11:30:00", "2023-09-15 12:15:00"),
# ]

# schema = ["order_id", "customer_id", "order_time", "payment_time"]
#
# df = spark.createDataFrame(data, schema)
#
# # Convert timestamp strings to Unix timestamps for easier calculation
# df = df.withColumn("order_timestamp", unix_timestamp("order_time"))
# df = df.withColumn("payment_timestamp", unix_timestamp("payment_time"))
#
# # Define a window specification to partition data by customer and order by order timestamp
# window_spec = Window.partitionBy("customer_id").orderBy("order_timestamp")
#
# # Calculate the time gap between the current order and the previous order
# df = df.withColumn("time_since_previous_order", col("order_timestamp") - lag("order_timestamp").over(window_spec))
#
# # Calculate the time gap between the current order and the next order
# df = df.withColumn("time_until_next_order", lead("order_timestamp").over(window_spec) - col("order_timestamp"))
#
# df.show()

# data = [("gunjan","kumar"),("Mona","Chandra")]
# schema = ["firstname","lastname"]
# df = spark.createDataFrame(data=data,schema=schema)
# df.show()
# df.withColumn("FullName",expr("firstname || lastname")).show()

data = [("James","M"),("Michael","F"),("Jen","")]
columns = ["name","gender"]
df = spark.createDataFrame(data = data, schema = columns)

df.show()

df2  = df.withColumn("NewGender",expr("case when gender='M' then 'Male' when gender='F' then 'Female' else 'Unknown' end"))
df2.show()
