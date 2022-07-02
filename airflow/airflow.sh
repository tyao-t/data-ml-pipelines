mkdir ~/airflow
export AIRFLOW_HOME=~/airflow
pip3 install --user apache-airflow
airflow initdb

cp /usr/local/notebooks/pipeline.py ~/airflow/dags/
airflow scheduler

airflow webserver -p 8080 
airflow list_dags
