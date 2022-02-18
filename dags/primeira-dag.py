import pendulum
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

local_tz=pendulum.timezone('America/Sao_Paulo')
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2022, 2, 17, 21, tzinfo=local_tz), 
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1, 
    'retry_delay': timedelta(seconds=30) 
}

dag = DAG(
    dag_id='primeira-dag-teste-pdi',
    default_args=default_args,
    schedule_interval='*/30 * * * *', 
    catchup=False,
    tags=['docker', 'pdi', 'airflow', 'carte', 'teste']
)

t1 = BashOperator(
    task_id='tsk-first-kettle-exec',
    bash_command='/opt/rep/dags/primeira_dag.sh ',
    dag=dag
)
