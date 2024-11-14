# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "fed97e2e-a913-4365-8a22-53f7d0bbbbf4",
# META       "default_lakehouse_name": "tcl_trip_lakehouse",
# META       "default_lakehouse_workspace_id": "1f17fff3-2c59-4e2c-8c6c-928ebf7f365b",
# META       "known_lakehouses": [
# META         {
# META           "id": "fed97e2e-a913-4365-8a22-53f7d0bbbbf4"
# META         },
# META         {
# META           "id": "2014010f-b370-44e2-b9c8-6d8fdf8e5124"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

spark.conf.set("spark.sql.parquet.vorder.enabled", "true")
spark.conf.set("spark.microsoft.delta.optimizeWrite.enabled", "true")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

pathBronze = "Files/bronze/yellow_taxi_tr/"
pathTables = "Tables/"

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df = spark.read.parquet(f"{pathBronze}yellow_tripdata_2024-01.parquet")
# display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

yellow_table_path = "silver_yellow_taxt_tr"
df.write.mode("append").format("delta").saveAsTable(yellow_table_path)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# df = spark.sql("SELECT * FROM tcl_trip_lakehouse.silver_yellow_taxt_tr LIMIT 1000")
# display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC select * from silver_yellow_taxt_tr

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }
