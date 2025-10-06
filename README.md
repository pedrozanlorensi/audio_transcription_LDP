## Audio Transcription with Lakeflow Declarative Pipelines (LDP)

This repo leverages LDPs with AI_QUERY to stream audio files from a Volume into a table with transcriptions.  

The transcriptions get generated using [Whisper](https://openai.com/index/whisper/), which is readily available in the system.ai schema of Databricks! 

Check out this blog post as a great reference for implementation: [Streamline Customer Call Center Transcripts Analytics with Mosaic AI Batch Inference](https://community.databricks.com/t5/technical-blog/streamline-customer-call-center-transcripts-analytics-with/ba-p/101689). Note that you need to serve the model using **Model Serving** and then you can call it with **AI_QUERY**.

The notebook **DownloadAudioToVolume.py** show a simple reference on how you can make HTTP requests to get audio files from a web server and then save it to a Volume.  
The folder **LDP** contains a notebook that is used to preprocess the files from the Volume into a silver table, and another notebook that is used to transcribe the audios into a gold table. 
