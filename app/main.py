import json
import datetime
from fastapi import FastAPI, Query
import google.auth
from google.cloud import bigquery

app = FastAPI(
    title="API Busters for Retail",
    description="API Busters for Retail",
    version="1.0.0",
    docs_url="/",
    redoc_url=None
)


def execBigquery(start_date: str, end_date: str):
    #query1 = "select * from for_ipl.api_busters_ecommerce_order_v where order_category = 'Historical_closed'  and status='Cancelled' and cast(created_at as date) between parse_date('%Y%m%d','{}') and parse_date('%Y%m%d','{}')"
    query1 = "select * from for_ipl.api_busters_ecommerce_order_v where order_category = 'Historical_closed'  and status='Cancelled' and cast(created_at as date) between parse_date('%Y%m%d','20220202') and parse_date('%Y%m%d','20220202')"
    query = query1.format(start_date,end_date)
    client = bigquery.Client()
    query_job = client.query(query)
    result_data = query_job.result()
    if result_data.total_rows > 0:
        result_df = result_data.to_dataframe()
        return json.loads(result_df.to_json(orient='records', date_format='iso', force_ascii=False))


@app.get("/get_historical_data")
def get_historical_orders_data(start_date: str = Query(..., alias="Start Date(YYYYMMDD)"),
                               end_date: str = Query(..., alias="End Date(YYYYMMDD)")):
    result_df = execBigquery(start_date,end_date)
    return result_df
