"""
This file contains a lambda function that is deployed on AWS
and runs the data cleaning script to produce the CSV output
"""

import json
from datetime import datetime
import pandas as pd
import awswrangler as wr

from constants import paths

from data_pipeline.extract import (
    extract_countries_data,
    extract_restaurants_data,
    extract_restaurant_records_from_parsed_json
)
from data_pipeline.transform import (
    process_restaurants,
    process_restaurant_events_within_date_range,
    prepare_data_for_q1,
    prepare_data_for_q2
)


def lambda_handler(event, context):
    """
    This is the entrypoint for the lambda function
    to run the data cleaning script for the CSV files
    """
    data = extract_restaurants_data()
    countries = pd.read_excel(paths.COUNTRY_CODE_LAMBDA_FILE_PATH)

    d_countries = extract_countries_data(countries)
    restaurant_records = extract_restaurant_records_from_parsed_json(data)

    rest_df = process_restaurants(d_countries, restaurant_records)
    events_df = process_restaurant_events_within_date_range(rest_df, "2019-04-01", "2019-04-30")

    q1_df = prepare_data_for_q1(rest_df)
    q2_df = prepare_data_for_q2(events_df)

    curr_time = datetime.now()
    q1_filename = f"q1_{curr_time}.csv"
    q2_filename = f"q2_{curr_time}.csv"

    filepath_q1 = f"s3://restaurants-output-bucket/{q1_filename}"
    filepath_q2 = f"s3://restaurants-output-bucket/{q2_filename}"

    wr.s3.to_csv(df=q1_df,path=filepath_q1)
    wr.s3.to_csv(df=q2_df,path=filepath_q2)

    print(event, context)

    return {
        'status_code': 200,
        'body': json.dumps('CSV files for Q1 and Q2 are exported!')
    }
