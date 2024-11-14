# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "2014010f-b370-44e2-b9c8-6d8fdf8e5124",
# META       "default_lakehouse_name": "tcl_trip_lakehouse",
# META       "default_lakehouse_workspace_id": "659e7793-6d0e-4d13-bf09-32503f437e53",
# META       "known_lakehouses": [
# META         {
# META           "id": "2014010f-b370-44e2-b9c8-6d8fdf8e5124"
# META         }
# META       ]
# META     }
# META   }
# META }

# MARKDOWN ********************

# #### Generación de tabla para la obtención de los ficheros necesarios desde 2009 hasta 2024-03

# CELL ********************

spark.conf.set("spark.sql.parquet.vorder.enabled", "true")
spark.conf.set("spark.microsoft.delta.optimizeWrite.enabled", "true")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

from pyspark.sql.functions import lit

# Definir los datasets y sus fechas de inicio
datasets = [
    ("Yellow Taxi Trip Records", "yellow_tripdata", "yellow_tripdata_", 2009, 1),
    ("Green Taxi Trip Records", "green_tripdata", "green_tripdata_", 2103, 8),
    ("For-Hire Vehicle Trip Records", "fhv_tripdata", "fhv_tripdata_", 2015, 1),
    ("High Volume For-Hire Vehicle Trip Records", "fhvhv_tripdata", "fhvhv_tripdata_", 2019, 2)
]

# Generar las combinaciones de datasets con las fechas correspondientes
data = []
for dataset_name, folder, file_prefix, start_year, start_month in datasets:
    year, month = start_year, start_month
    while (year < 2024) or (year == 2024 and month <= 3):
        date_str = f"{year:04d}-{month:02d}"
        file_name = f"{file_prefix}{date_str}.parquet"
        data.append((dataset_name, file_name, folder, date_str, 1))
        if month == 12:
            year += 1
            month = 1
        else:
            month += 1

# Convertir la lista en un DataFrame de PySpark
columns = ["dataset_name", "file_name", "file_folder", "date", "enabledToLoad"]
df = spark.createDataFrame(data, columns)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

system_config_tables = "system_config_tables"
df.write.mode("overwrite").format("delta").saveAsTable(system_config_tables)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql 
# MAGIC select * from system_config_tables

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }
