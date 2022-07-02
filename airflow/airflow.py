from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_args = {
   'owner': 'Airflow',
   'depends_on_past': False,
   'email': 'tianhaoyao00@gmail.com',
   'start_date': datetime(2022, 6, 1),
   'email_on_failure': True,
}

dag = DAG('games', default_args=default_args, schedule_interval="* * * * *")

t1 = BashOperator(
    task_id='sklearn_etl',
    bash_command='sudo docker run sklearn_etl',
    dag=dag)

t2 = BashOperator(
    task_id='sklearn_pipeline',
    bash_command='sudo docker run sklearn_pipeline',
    dag=dag)

t2.set_upstream(t1)