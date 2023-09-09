"""
This file contains the main script to run 
so as to initiate the data cleaning process
"""

from datetime import datetime
import pandas as pd
from data_pipeline import (
    extract_countries_data,
    extract_restaurants_data,
    extract_restaurant_records_from_parsed_json,
    process_restaurants,
    prepare_data_for_q1
)

if __name__ == '__main__':
    print("=======================================================")
    print("Data processing script for restaurants data from Zomato")
    print("=======================================================")

    data = extract_restaurants_data()
    print("- Restaurants data is read")

    countries = pd.read_excel('./data_files/Country-Code.xlsx')
    print("- Countries data is read")

    d_countries = extract_countries_data(countries)
    restaurant_records = extract_restaurant_records_from_parsed_json(data)

    df1 = process_restaurants(d_countries, restaurant_records)

    print("-The dataframes for Q1 is processed")
    q1_df = prepare_data_for_q1(df1)

    curr_time = datetime.now()
    q1_filename = f"sample_output/q1_{curr_time}.csv"

    print("\n")
    print("=========================")
    print("Preview of Q1's dataframe")
    print("=========================")
    print(q1_df.head(5))
    print("\n")
