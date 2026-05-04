import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col, lower, to_date, coalesce, lit, when

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

datasource = glueContext.create_dynamic_frame.from_catalog(
    database="inventory_db",
    table_name="kito_raw_data"
)

df = datasource.toDF()
df = df.dropDuplicates()

# Drop NULL quantity rows
df = df.filter(col("quantity").isNotNull())

# fix and handle date format
df = df.withColumn("order_date",
    coalesce(
        to_date(col("order_date"), "yyyy/MM/dd"),
        to_date(col("order_date"), "MM-dd-yyyy"),
        to_date(col("order_date"), "MM/dd/yyyy")
    )
)

# lowercase regions
df = df.withColumn("region", lower(col("region")))

# new total value column
df = df.withColumn("total_value", col("quantity") * col("price"))

# Write output as Parquet to curated S3 bucket
df.write.mode("overwrite").parquet("s3://kito-curated-data/cleaned/")

job.commit()
