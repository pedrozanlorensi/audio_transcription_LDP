# Databricks notebook source
import dlt
import pyspark.sql.functions as F

# COMMAND ----------

# Create the silver dataset
@dlt.table(
    name="pedroz_genai_catalog.audio.silver_audio_preprocessed",
    comment="Streaming table of audios with metadata"
)
def silver_audio_preprocessed():
    # Stream images in binary format
    df = spark.readStream.format("cloudFiles")   \
        .option("cloudFiles.format", "binaryFile") \
        .option("pathGlobFilter", "*.wav") \
        .load("/Volumes/pedroz_genai_catalog/audio/speech_data")

    # Save image binary content into column img
    df = df.withColumn("audio", F.col("content"))

    return df.select(
        "path",
        "modificationTime",
        "length",
        "audio"
    )