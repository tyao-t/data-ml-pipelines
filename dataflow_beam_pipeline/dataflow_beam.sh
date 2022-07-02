#!bin/bash

#pip3 install apache-beam[gcp]
#export GOOGLE_APPLICATION_CREDENTIALS=dsdemo.json
#python3 -m apache_beam.examples.wordcount --output outputs

# running locally 
python3 apply.py --project your_project_id

# running on GCP 
echo $'google-cloud-storage==1.19.0' > reqs.txt
python3 apply.py \
  --runner DataflowRunner \
  --project your_project_id \
  --temp_location gs://dsp_model_store/tmp/ \
  --requirements_file reqs.txt \
  --max_num_workers 5  