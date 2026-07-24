#Import Libraries
from pyspark import pipelines as dp
from pyspark.sql.types import *
from pyspark.sql.functions import current_timestamp

@dp.materialized_view(
  comment="Raw data on employee")
def employee():
  # Read parameters inside the function so they're evaluated per run
  emp_id = spark.conf.get("id", "1")
  name = spark.conf.get("name", "test")
  
  data = [(emp_id, name, current_timestamp())]
  schema = ["employee_id", "employee_name", "load_time"]
  
  return spark.createDataFrame(data, schema)
