# Run with Dataflow
python3 pubsub_dataflow_beam_sklearn_pipeline.py --streaming --runner DataflowRunner --project my_project_name --temp_location gs://streaming_pipeline/tmp/ 

#PATH=/usr/local/google-cloud-sdk/bin:$PATH && cd /usr/local/notebooks/ && export GOOGLE_APPLICATION_CREDENTIALS=creds.json && gcloud auth activate-service-account --key-file=creds.json --project=$PROJECT_ID

# Run locally
python3 pubsub_dataflow_beam_sklearn_pipeline.py --streaming