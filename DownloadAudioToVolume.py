# Databricks notebook source
# Pythonic way that references Volumes as a regular element of your file system

import requests

url = "https://github.com/Nexdata-AI/104-Hours-Brazilian-Portuguese-Conversational-Speech-Data-by-Telephone/raw/refs/heads/main/0001_001_telephone-1.wav"
response = requests.get(url)
response.raise_for_status()

volume_path = "/Volumes/pedroz_genai_catalog/audio/speech_data/uploads/0001_001_telephone-1.wav"
with open(volume_path, "wb") as f:
    f.write(response.content)

# COMMAND ----------

# Using the Databricks SDK

import requests
from databricks.sdk import WorkspaceClient

url = "https://github.com/Nexdata-AI/104-Hours-Brazilian-Portuguese-Conversational-Speech-Data-by-Telephone/raw/refs/heads/main/0001_001_telephone-1.wav"
response = requests.get(url)
response.raise_for_status()

volume_path = "/Volumes/pedroz_genai_catalog/audio/speech_data/uploads/0001_001_telephone-1.wav"
w = WorkspaceClient()
w.files.upload(volume_path, response.content, overwrite=True)