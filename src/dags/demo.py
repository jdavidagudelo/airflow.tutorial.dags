from datetime import datetime

import pytz
from airflow import DAG
from airflow.decorators import task
from airflow.operators.bash import BashOperator

# A DAG represents a workflow, a collection of tasks
with DAG(dag_id="demo", start_date=datetime(2024, 4, 6, tzinfo=pytz.UTC), schedule="0 * * * *") as dag:
    # Tasks are represented as operators
    hello = BashOperator(task_id="hello", bash_command="echo hello")

    @task()
    def airflow():
        print("airflow")  # noqa: T201

    # Set dependencies between tasks
    hello >> airflow()
