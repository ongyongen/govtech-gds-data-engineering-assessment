"""
This file contains methods used in the Transform phase of the ETL pipeline
"""

from constants import dataframe
from data_pipeline.helpers import (
    create_template_restaurants_df,
    map_country_code_to_country_name
)

def process_restaurants(d_countries, restaurant_records):
    """
    Collect restaurant record data into the template dataframe for
    cleaned restaurants data

    Input : dictionary, list
    Output : dataframe 
    """

    data_frame = create_template_restaurants_df()

    for index, record in enumerate(restaurant_records):
        restaurant = record["restaurant"]
        data_frame.loc[index, dataframe.RESTAURANT_ID] = restaurant["R"]["res_id"]
        data_frame.loc[index, dataframe.RESTAURANT_NAME] = restaurant["name"]
        data_frame.loc[index, dataframe.COUNTRY_ID] = restaurant["location"]["country_id"]
        data_frame.loc[index, dataframe.CITY] = restaurant["location"]["city"]
        data_frame.loc[index, dataframe.USER_RATING_VOTES] = restaurant["user_rating"]["votes"]
        data_frame.loc[index, dataframe.USER_AGGREGATE_RATING] = \
            restaurant["user_rating"]["aggregate_rating"]
        data_frame.loc[index, dataframe.CUISINES] = restaurant["cuisines"]
        data_frame.loc[index, dataframe.RATING_TEXT] = restaurant["user_rating"]["rating_text"]

        # Use the d_countries dictionary to map country code to country name
        data_frame.loc[index, dataframe.COUNTRY] = map_country_code_to_country_name(
            d_countries, restaurant["location"]["country_id"])

        # If current reecord has an events list, add it to dataframe's "events" column
        # If not, add an empty list to dataframe's "events" column
        if "zomato_events" in record["restaurant"]:
            events = restaurant["zomato_events"]
            data_frame.at[index, dataframe.EVENTS] = events
        else:
            data_frame.at[index, dataframe.EVENTS] = dataframe.EMPTY_EVENTS_CELL

    return data_frame
