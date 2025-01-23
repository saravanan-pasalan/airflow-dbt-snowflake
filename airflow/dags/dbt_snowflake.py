from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator
from airflow.utils.task_group import TaskGroup
from datetime import datetime

PROJECT_DIR ='/mnt/c/Users/psara/shrovandbtsnowflake'
PROFILES_DIR='/mnt/c/Users/psara/.dbt'

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'retries': 3,
}

with DAG(
    'airflow_dbt_snowflake3',
    default_args=default_args,
    description='Airflow job to run dbt-snowflake from airflow',
    schedule_interval='@daily',
    start_date=datetime(2024,1,22),
    catchup=False,
) as dag:


    start = EmptyOperator(task_id='start_dag')

    with TaskGroup(group_id='dbt_tasks') as dbt_tasks:
        dbt_debug = BashOperator(
            task_id='dbt-debug',
            bash_command=f'dbt debug --profiles-dir {PROFILES_DIR} --project-dir {PROJECT_DIR}',   
        )

        #dbt run task
        dbt_run = BashOperator(
            task_id='dbt-run',
            #bash_command=f'dbt run --profiles-dir {PROFILES_DIR} --project-dit {PROJECT_DIR}'   
            bash_command=f'dbt run --profiles-dir {PROFILES_DIR} --project-dir {PROJECT_DIR}',
        )

        dbt_debug >> dbt_run

    end = EmptyOperator(task_id='end_dag')

    #Task Dependencies
    start>>dbt_tasks>>end
