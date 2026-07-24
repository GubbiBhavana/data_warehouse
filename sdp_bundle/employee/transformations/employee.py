#Import Libraries
from pyspark import pipelines as dp
from pyspark.sql.types import *

# Import data from parameters
emp_id = spark.conf.get("id", "1")
name = spark.conf.get("name", "default")

data = [(emp_id, name, NOW()),]
schema = ["employee_id","employee_name","load_time"]

@dp.materialized_view(
  comment="Raw data on employee")
  
def sales():
  return spark.createDataFrame(
    data,
    schema
  )
