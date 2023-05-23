import json
#import logging
from fastapi import FastAPI
import google.auth
from google.cloud import bigquery
import pandas
#from google.cloud.bigquery.table import TimePartitioning

#logger = logging.getLogger()
#logger.setLevel(logging.ERROR)
#from google.oauth2 import service_account
#import os 

#destination_project = "gcp-project-100"
#destination_dataset = "Test"

app = FastAPI(
    title="API Busters for Retail",
    description="API Busters for Retail",
    version="1.0.0",
    docs_url="/",
    redoc_url=None
)


def execBigquery():
    query = "select * from for_ipl.api_busters_ecommerce_order_v where order_category = 'Historical'"
    client = bigquery.Client()
    query_job = client.query(query)
    result_data = query_job.result()
    if result_data.total_rows > 0:
        df = result_data.to_dataframe()
        return df.to_json(orient='records', force_ascii=False)


@app.get("/get_historical_data")
def get_historical_orders_data():
    result_df = execBigquery()
    return result_df
