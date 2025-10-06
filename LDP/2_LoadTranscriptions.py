# Databricks notebook source
import dlt
from pyspark.sql.functions import expr

# COMMAND ----------

# Create the silver dataset
@dlt.table(
    name="pedroz_genai_catalog.audio.gold_audio_transcribed",
    comment="Streaming table of transcribed audios"
)
def silver_audio_preprocessed():
    # Read from the silver table
    df = dlt.read_stream("pedroz_genai_catalog.audio.silver_audio_preprocessed")

    # Transcribe the audio content
    df = df.withColumn(
        "transcription",
        expr(
            """
            AI_QUERY(
                "whisper_large_v3",
                audio
            )
            """
        )
    )

    return df.select(
        "path",
        "transcription"
    )