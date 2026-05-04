# AWS Glue ETL Pipeline — Supply Chain Analytics

## Overview
A lightweight serverless ETL pipeline built with AWS Glue and Amazon Athena to process messy supply chain inventory data into output.

## Pipeline Architecture
S3 (Raw CSV) → Glue Crawler → Glue ETL Job → S3 (Parquet) → Athena (SQL)

## AWS Services Used
- Amazon S3 — raw and curated data storage
- AWS Glue Crawler — schema discovery and cataloging
- AWS Glue ETL — PySpark transformations
- Amazon Athena — serverless SQL querying

## Transformations Applied
- Removed duplicate rows
- Dropped rows with null quantity
- Standardized inconsistent date formats
- Normalized region field to lowercase
- Added derived column: total_value

## How to Run
1. Upload the raw data file to your S3 raw bucket
2. Run the Glue Crawler pointing at the raw bucket
3. Run the Glue ETL job transform.py
4. Run second Glue Crawler pointing at curated bucket
5. Query results in Athena using SQL queries

## Sample Athena Query Results
<img width="975" height="1024" alt="image" src="https://github.com/user-attachments/assets/3da5db2d-6c4e-4805-8c7e-231b7eeebad5" />
