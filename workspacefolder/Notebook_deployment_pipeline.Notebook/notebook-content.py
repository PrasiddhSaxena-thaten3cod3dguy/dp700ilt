# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "32c0ca80-5b9c-4ba5-9640-0fefc7ca3b86",
# META       "default_lakehouse_name": "lakehouse_deploy_pipeline",
# META       "default_lakehouse_workspace_id": "47196744-c3f3-412e-9a6f-ae76e38a3eca",
# META       "known_lakehouses": [
# META         {
# META           "id": "32c0ca80-5b9c-4ba5-9640-0fefc7ca3b86"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df = spark.read.format("csv").option("header","true").load("Files/sales.csv")
# df now is a Spark DataFrame containing CSV data from "Files/sales.csv".
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
