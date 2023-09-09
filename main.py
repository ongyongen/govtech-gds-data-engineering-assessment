"""
This file contains the main script to run 
so as to initiate the data cleaning process
"""

import pandas as pd
from data_pipeline import (
    extract_countries_data,
    extract_restaurants_data,
    extract_restaurant_records_from_parsed_json,
    process_restaurants,
    process_restaurant_events_within_date_range,
    prepare_data_for_q1,
    prepare_data_for_q2,
)

def run_script():
    """
    Outputs results to the console when user runs
    python main.py in their terminal

    Input : None
    Output : String printed to the terminal
    """

    print("\n")
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
    df2 = process_restaurant_events_within_date_range(df1, '2019-04-01', '2019-04-30')

    print("- The dataframes for Q1 and Q2 are processed")
    q1_df = prepare_data_for_q1(df1)
    q2_df = prepare_data_for_q2(df2)

    # curr_time = datetime.now()
    # q1_filename = f"sample_output/q1_{curr_time}.csv"
    # q2_filename = f"sample_output/q2_{curr_time}.csv"

    # df1.to_csv(q1_filename)
    # df2.to_csv(q2_filename)
    print("- The dataframes for Q1 and Q2 are exported to sample_output folder")

    print("\n")
    print("=========================")
    print("Preview of Q1's dataframe")
    print("=========================")
    print(q1_df.head(5))
    print("\n")

    print("=========================")
    print("Preview of Q2's dataframe")
    print("=========================")
    print(q2_df.head(5))
    print("\n")

    print("=========================")
    print("Q3 Analysis")
    print("=========================")
    print("\n")


if __name__ == '__main__':
    run_script()
    