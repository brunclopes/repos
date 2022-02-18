import pendulum
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

local_tz=pendulum.timezone('America/Sao_Paulo')
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2022, 2, 17, 19, tzinfo=local_tz), #Exemplo: Inicia em 2 de Setembro de 2021, a partir das 19h
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1, #Em caso de erros, tente rodar novamente apenas 1 vez
    'retry_delay': timedelta(seconds=30) #Tente novamente apos 30 segundos depois do erro
}

dag = DAG(
    dag_id='dag-first-kettle-exec',
    default_args=default_args,
    schedule_interval='*/5 * * * *', #Execute uma vez a cada 5 minutos
    catchup=False,
    tags=['docker', 'pdi', 'airflow', 'carte', 'bootcamp']
)

t1 = BashOperator(
    task_id='tsk-first-kettle-exec',
    bash_command='/opt/repos/dags/first_dag.sh ',
    dag=dag
)
