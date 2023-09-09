"""
This file contains mock data for data pipeline - helpers' function's
testing 
"""
import pandas as pd
from constants import dataframe

# Mock data for : test_replace_na_cells
mock_one_replace_na_cells = pd.DataFrame(columns=["A","B"])
mock_one_replace_na_cells.loc[0,"A"] = None
mock_one_replace_na_cells.loc[0,"B"] = None

mock_two_replace_na_cells = pd.DataFrame(columns=["C","D"])
mock_two_replace_na_cells.loc[0,"C"] = None
mock_two_replace_na_cells.loc[0,"D"] = None

# Mock data for : test_extract_photo_urls
mock_one_extract_photo_urls = {
    "photos": []
}

mock_two_extract_photo_urls = {
    "photos": [
        {"photo": {'url': "1"}},
        {"photo": {'url': "2"}},
        {"photo": {'url': "3"}}
    ]
}

mock_three_extract_photo_urls = {
    "photos": [
        {"photo": {'url': "1"}}
    ]
}

# Mock data for : test_map_country_code_to_country_name
mock_d_countries_map_country_code_to_country_name = {
    1 : "Singapore",
    2 : "Malaysia",
    3 : "Indonesia"
}

# Mock data for : test_max_score_for_rating and test_min_score_for_rating
mock_data_test_scores_for_rating = [
    {
      dataframe.RESTAURANT_ID: 18649486.0,
      dataframe.RESTAURANT_NAME: "The Botanist",
      dataframe.COUNTRY_ID: 1,
      dataframe.CITY: "Gurgaon",
      dataframe.USER_RATING_VOTES: "47650",
      dataframe.USER_AGGREGATE_RATING: "4.9",
      dataframe.CUISINES: "Chinese",
      dataframe.RATING_TEXT: "Excellent",
      dataframe.COUNTRY: "India",
      dataframe.EVENTS: [],
    },
    {
      dataframe.RESTAURANT_ID: 18649482.0,
      dataframe.RESTAURANT_NAME: "The Drunken Botanist 1",
      dataframe.COUNTRY_ID: 1,
      dataframe.CITY: "Gurgaon",
      dataframe.USER_RATING_VOTES: "8888",
      dataframe.USER_AGGREGATE_RATING: "4.4",
      dataframe.CUISINES: "Continental, Chinese",
      dataframe.RATING_TEXT: "Very Good",
      dataframe.COUNTRY: "India",
      dataframe.EVENTS: [],
    },
    {
      dataframe.RESTAURANT_ID: 18649487.0,
      dataframe.RESTAURANT_NAME: "The Drunken Botanist 2",
      dataframe.COUNTRY_ID: 1,
      dataframe.CITY: "Gurgaon",
      dataframe.USER_RATING_VOTES: "3367",
      dataframe.USER_AGGREGATE_RATING: "4.0",
      dataframe.CUISINES: "Italian, North Indian",
      dataframe.RATING_TEXT: "Good",
      dataframe.COUNTRY: "India",
      dataframe.EVENTS: [],
    },
    {
      dataframe.RESTAURANT_ID: 18649487.0,
      dataframe.RESTAURANT_NAME: "The Drunken Botanist 3",
      dataframe.COUNTRY_ID: 1,
      dataframe.CITY: "Gurgaon",
      dataframe.USER_RATING_VOTES: "4768",
      dataframe.USER_AGGREGATE_RATING: "4.7",
      dataframe.CUISINES: "North Indian, Chinese",
      dataframe.RATING_TEXT: "Excellent",
      dataframe.COUNTRY: "India",
      dataframe.EVENTS: [],
    },
    {
      dataframe.RESTAURANT_ID: 18649488.0,
      dataframe.RESTAURANT_NAME: "The Drunken Botanist 4",
      dataframe.COUNTRY_ID: 1,
      dataframe.CITY: "Gurgaon",
      dataframe.USER_RATING_VOTES: "4769",
      dataframe.USER_AGGREGATE_RATING: "2.0",
      dataframe.CUISINES: "Continental, Italian",
      dataframe.RATING_TEXT: "Poor",
      dataframe.COUNTRY: "India",
      dataframe.EVENTS: [],
    },
    {
      dataframe.RESTAURANT_ID: 18649484.0,
      dataframe.RESTAURANT_NAME: "The Drunken Botanist 5",
      dataframe.COUNTRY_ID: 1,
      dataframe.CITY: "Gurgaon",
      dataframe.USER_RATING_VOTES: "4770",
      dataframe.USER_AGGREGATE_RATING: "2.4",
      dataframe.CUISINES: "Chinese",
      dataframe.RATING_TEXT: "Poor",
      dataframe.COUNTRY: "India",
      dataframe.EVENTS: [],
    },
    {
      dataframe.RESTAURANT_ID: 18649481.0,
      dataframe.RESTAURANT_NAME: "The Drunken Botanist 6",
      dataframe.COUNTRY_ID: 1,
      dataframe.CITY: "Gurgaon",
      dataframe.USER_RATING_VOTES: "4711",
      dataframe.USER_AGGREGATE_RATING: "3.5",
      dataframe.CUISINES: "Continental, Italian, North Indian, Chinese",
      dataframe.RATING_TEXT: "Average",
      dataframe.COUNTRY: "India",
      dataframe.EVENTS: [],
    }
]

mock_df_test_scores_for_rating = pd.DataFrame(
    mock_data_test_scores_for_rating
)
