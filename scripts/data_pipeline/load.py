"""
This file contains methods used in the Load phase of the ETL pipeline
"""
import pandas as pd
from constants import dataframe, q3_output
from .helpers import min_score_for_rating, max_score_for_rating

def export_dataframe_to_csv(final_dataframe, csv_file_path):
    """
    Convert a dataframe into a CSV file for export

    Input : dataframe, string
    Output : None
    """
    final_dataframe.to_csv(csv_file_path)

def print_output_for_q3(restaurants_dataframe):
    """
    Print explanation of the thresholds for
    the different rating texts as part of Q3

    Input : dataframe (from process_restaurants)
    Output : None
    """

    data = {
        "Minimum Rating Score": [
            min_score_for_rating(restaurants_dataframe, dataframe.POOR),
            min_score_for_rating(restaurants_dataframe, dataframe.AVERAGE),
            min_score_for_rating(restaurants_dataframe, dataframe.GOOD),
            min_score_for_rating(restaurants_dataframe, dataframe.VERY_GOOD),
            min_score_for_rating(restaurants_dataframe, dataframe.EXCELLENT),
        ],
        "Maximum Rating Score" : [
            max_score_for_rating(restaurants_dataframe, dataframe.POOR),
            max_score_for_rating(restaurants_dataframe, dataframe.AVERAGE),
            max_score_for_rating(restaurants_dataframe, dataframe.GOOD),
            max_score_for_rating(restaurants_dataframe, dataframe.VERY_GOOD),
            max_score_for_rating(restaurants_dataframe, dataframe.EXCELLENT),
        ]
    }

    df_index = [
        "Poor",
        "Average",
        "Good",
        "Very Good",
        "Excellent"
    ]

    # Creates pandas DataFrame.
    df_q3 = pd.DataFrame(data, index=df_index)

    rating_categories = set(restaurants_dataframe[dataframe.RATING_TEXT])
    print(f"Rating categories: {rating_categories}")

    print(q3_output.PARA_ONE)
    print(df_q3)
    print(q3_output.PARA_TWO)
    print(q3_output.DF_Q3_THRESHOLDS)
