import json
import logging
from fastapi import FastAPI
import google.auth
from google.cloud import bigquery
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
    result = client.query(query)
    #query_job.result()
    result_dict = {'data' : result}
    result_json_data = json.dumps(result_dict)
    return result_json_data

@app.get("/get_historical_data")
def get_historical_orders_data():
    historical_data = execBigquery()
    return historical_data
