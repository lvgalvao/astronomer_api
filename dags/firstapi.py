"""
firstapi
DAG auto-generated by Astro Cloud IDE.
"""

from airflow.decorators import dag
from airflow.models import Variable
from astro import sql as aql
import pandas as pd
import pendulum

from airflow.models import Variable
import requests
import random

@aql.dataframe(task_id="gerar_numer_aleatorio")
def gerar_numer_aleatorio_func():
    return random.randint(1, 100)

@aql.dataframe(task_id="pegar_api")
def pegar_api_func(gerar_numer_aleatorio: pd.DataFrame):
    FULL_URL = str(Variable.get("API")) + "/" + str(gerar_numer_aleatorio)
    r = requests.get(FULL_URL)
    return r.json()["name"]

@aql.dataframe(task_id="print")
def print_func(pegar_api: pd.DataFrame):
    print(pegar_api)

default_args={
    "owner": "Luciano Filho,Open in Cloud IDE",
}

@dag(
    default_args=default_args,
    schedule="0 0 * * *",
    start_date=pendulum.from_format("2024-03-23", "YYYY-MM-DD").in_tz("UTC"),
    catchup=False,
    owner_links={
        "Luciano Filho": "mailto:lvgalvaofilho@gmail.com",
        "Open in Cloud IDE": "https://cloud.astronomer.io/clu3h21wy071k01pra3nb36mj/cloud-ide/clu3nchkd073s01prfx75elaw/clu3nkzoa077k01m33udmvdp1",
    },
)
def firstapi():
    gerar_numer_aleatorio = gerar_numer_aleatorio_func()

    pegar_api = pegar_api_func(
        gerar_numer_aleatorio,
    )

    print = print_func(
        pegar_api,
    )

dag_obj = firstapi()
