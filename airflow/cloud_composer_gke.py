from airflow.gcp.operators.kubernetes_engine import GKEPodOperator

t1 = GKEPodOperator(
    task_id='sklearn_pipeline',
    project_id = '{my_project_id}',
    cluster_name = ' us-central1-models-13d59d5b-gke',
    name ='sklearn_pipeline',
    namespace='default',
    location='us-central1-c',
    image='us.gcr.io/{my_project_id}/sklearn_pipeline',
    dag=dag)
