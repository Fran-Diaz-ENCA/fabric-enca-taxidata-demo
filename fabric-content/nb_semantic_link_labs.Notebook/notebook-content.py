# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "343a6292-9110-4606-bef1-289e561a2fa6",
# META       "default_lakehouse_name": "lh_AdventureWorks_mirror",
# META       "default_lakehouse_workspace_id": "41ef6a76-8469-4c7e-ab3d-ecb66e584373"
# META     },
# META     "environment": {}
# META   }
# META }

# MARKDOWN ********************

# ### Notebook para obtener información de las apis de Fabric


# CELL ********************

%pip install semantic-link-labs

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

import sempy_labs as labs
from sempy_labs import migration, directlake, admin
from sempy_labs import lakehouse as lake
from sempy_labs import report as rep
from sempy_labs.tom import connect_semantic_model
from sempy_labs.report import ReportWrapper
from sempy_labs import ConnectWarehouse
from sempy_labs import ConnectLakehouse

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# #### Mirroring

# CELL ********************

labs.list_mirrored_databases(None)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Obtenemos el estado del mirroring
labs.get_mirroring_status("AdventureWorksLT-Free")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

labs.get_tables_mirroring_status('AdventureWorksLT-Free',None)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

#Encendemos
#labs.start_mirroring

#Paramos
#labs.stop_mirroring

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

definit = labs.get_mirrored_database_definition('AdventureWorksLT-Free', workspace=None)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# #### Listamos el número de lakehouses que hay en un workspace concreto. 

# CELL ********************

labs.list_lakehouses("ws-fabric-mirroring-demo-dev")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Obtenemos el id del lakehouse a partir del nombre de este.
labs.resolve_lakehouse_id('lh_AdventureWorks_mirror',None)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Obtenemos el nombre del lakehouse a través del id del este.
labs.resolve_lakehouse_name('343a6292-9110-4606-bef1-289e561a2fa6')

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# #### Lista los workspaces especificados. 


# CELL ********************

df_workspaces = labs.admin.list_workspaces()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df_spark = spark.createDataFrame(df_workspaces)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Filtrar el DataFrame usando una expresión SQL en el filtro
df = df_spark.filter("Name = 'ws-fabric-mirroring-demo-dev'")
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# #### Listado de conexiones

# CELL ********************

df_conn = spark.createDataFrame(labs.list_connections())
display(df_conn)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Más info de los items: https://learn.microsoft.com/es-es/rest/api/fabric/core/items/update-item?tabs=HTTP#itemtype
labs.list_item_connections('lh_AdventureWorks_mirror','Lakehouse',None)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
