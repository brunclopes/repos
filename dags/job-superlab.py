#Roda o carte.job
import pendulum
from datetime import datetime, timedelta
from airflow import DAG
from airflow_pentaho.operators.CarteJobOperator import CarteJobOperator

local_tz=pendulum.timezone('America/Sao_Paulo')

default_args = {
    'owner': 'bootcamp',
    'depends_on_past': False,
    'start_date': datetime(2021, 9, 2, 20, tzinfo=local_tz), #datetime(yyyy,mm,dd,hh,mn,sc, tzinfo=local_tz),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(seconds=30)
}

dag = DAG(
    dag_id='dag-job-superlab-exec',
    default_args=default_args,
    schedule_interval='*/1 * * * *',
    catchup=False,
    tags=['docker', 'pdi', 'airflow', 'carte', 'bootcamp']
)

job = CarteJobOperator(
    dag=dag,
    task_id='tsk-job-superlab-exec',
    job='/superlab/main_dataset2_sales',
    level= 'Basic'
)