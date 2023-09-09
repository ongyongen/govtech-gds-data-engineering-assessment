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
    print_output_for_q3,
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

    print("- Extracting restaurants data")
    data = extract_restaurants_data()
    countries = pd.read_excel('./data_files/Country-Code.xlsx')

    d_countries = extract_countries_data(countries)
    restaurant_records = extract_restaurant_records_from_parsed_json(data)

    print("- Processing dataframes for Q1 and Q2")
    df1 = process_restaurants(d_countries, restaurant_records)
    df2 = process_restaurant_events_within_date_range(df1, '2019-04-01', '2019-04-30')

    print("- Exporting dataframes for Q1 and Q2 into sample_output folder")
    q1_df = prepare_data_for_q1(df1)
    q2_df = prepare_data_for_q2(df2)

    # curr_time = datetime.now()
    # q1_filename = f"sample_output/q1_{curr_time}.csv"
    # q2_filename = f"sample_output/q2_{curr_time}.csv"

    # export_dataframe_to_csv(q1_df, q1_filename)
    # export_dataframe_to_csv(q2_df, q2_filename)

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
    print_output_for_q3(df1)
    print("\n")


if __name__ == '__main__':
    run_script()
    