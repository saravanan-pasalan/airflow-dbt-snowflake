from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def helloworld():
    print('Hello world')

with DAG(dag_id="first_dag",
        start_date=datetime(2025,1,22),
        schedule_interval='@hourly',
        catchup=False) as dag:

        task1 = PythonOperator(
        task_id="Hello_world",
        python_callable=helloworld)
        
task1

