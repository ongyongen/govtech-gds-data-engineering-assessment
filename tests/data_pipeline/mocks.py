"""
This file contains mock data for data pipeline - extract's function's
testing 
"""

import pandas as pd

# Mock data for : extract_restaurant_records_from_parsed_json 
mock_one_extract_restaurant_records_from_parsed_json = [
    {
        "results_found" : 0,
        "results_start" : 0,
        "results_shown" : 0,
        "restaurants" : [
        ]
    }
]

mock_two_extract_restaurant_records_from_parsed_json = [
    {
        "results_found" : 4,
        "results_start" : 4,
        "results_shown" : 4,
        "restaurants" : [
            {"restaurant" : ""},
            {"restaurant" : ""},
            {"restaurant" : ""},
            {"restaurant" : ""},
        ]
    }
]

# Mock data for : extract_countries_data
mock_one_countries_data = [
    {
        "Country Code": 1, 
        "Country": "United States"
    },
    {
        "Country Code": 2, 
        "Country": "Singapore"
    },
    {
        "Country Code": 3, 
        "Country": "China"
    },
]
mock_one_df_extract_countries_data = pd.DataFrame(mock_one_countries_data)
mock_one_df_expected_extract_countries_data = {
    1 : "United States",
    2 : "Singapore",
    3 : "China"
}

mock_two_df_extract_countries_data = pd.DataFrame()
mock_two_df_expected_extract_countries_data = {}
