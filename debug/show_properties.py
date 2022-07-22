# Databricks notebook source
db = "christopherchalcraft_scratch"

spark.sql(f"CREATE DATABASE IF NOT EXISTS {db}")
spark.sql(f"USE {db}")

# spark.sql("SET spark.databricks.delta.formatCheck.enabled = false")
# spark.sql("SET spark.databricks.delta.properties.defaults.autoOptimize.optimizeWrite = true")

# COMMAND ----------

# MAGIC %sql
# MAGIC show tblproperties temp_delta
