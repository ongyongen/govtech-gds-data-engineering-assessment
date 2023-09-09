"""
This file contains helper methods used throughout the phases of the ETL pipeline
"""

from datetime import datetime
import pandas as pd
from constants import dataframe

def create_template_restaurants_df():
    """
    Create a template dataframe for the cleaned restaurants data
    (used for Q1 CSV output)

    Input : None
    Output : dataframe 
    """
    columns = {
        dataframe.RESTAURANT_ID: pd.Series(dtype='int'),
        dataframe.RESTAURANT_NAME: pd.Series(dtype='str'),
        dataframe.COUNTRY: pd.Series(dtype='str'),
        dataframe.CITY: pd.Series(dtype='str'),
        dataframe.USER_RATING_VOTES: pd.Series(dtype='str'),
        dataframe.USER_AGGREGATE_RATING: pd.Series(dtype='str'),
        dataframe.CUISINES: pd.Series(dtype='str'),
        dataframe.COUNTRY_ID: pd.Series(dtype='int'),
        dataframe.RATING_TEXT: pd.Series(dtype='str'),
        dataframe.PHOTO_URL: pd.Series(dtype='str'),
        dataframe.EVENTS: pd.Series(dtype='object'),
        dataframe.EVENT_ID: pd.Series(dtype='str'),
        dataframe.EVENT_TITLE: pd.Series(dtype='str'),
        dataframe.EVENT_START_DATE: pd.Series(dtype='str'),
        dataframe.EVENT_END_DATE: pd.Series(dtype='str')
    }

    data_frame = pd.DataFrame(columns)
    return data_frame

def create_template_events_df():
    """
    Create a template dataframe for the cleaned restaurant events data
    in Apr 2019 (used for Q2 CSV output)

    Input : None
    Output : dataframe 
    """
    columns = {
        dataframe.EVENT_ID: pd.Series(dtype='str'),
        dataframe.RESTAURANT_ID: pd.Series(dtype='int'),
        dataframe.RESTAURANT_NAME: pd.Series(dtype='str'),
        dataframe.PHOTO_URL: pd.Series(dtype='str'),
        dataframe.EVENT_TITLE: pd.Series(dtype='str'),
        dataframe.EVENT_START_DATE: pd.Series(dtype='str'),
        dataframe.EVENT_END_DATE: pd.Series(dtype='str'),
    }

    data_frame = pd.DataFrame(columns)
    return data_frame

def replace_na_cells(data_frame, replacement_str):
    """
    Replace NaN cells in the dataframe with a provided
    replacement string

    Input : dataframe, string 
    Output : dataframe 
    """
    data_frame = data_frame.fillna(replacement_str)
    return data_frame

def event_occurs_within_dates(
    event_start,
    event_end,
    fixed_start,
    fixed_end
):
    """
    Check whether an event occurs within a date range 

    Input : string, string, string, string
    Output : boolean 
    """
    date_pattern = "%Y-%m-%d"
    event_start_dt = datetime.strptime(event_start, date_pattern)
    event_end_dt = datetime.strptime(event_end, date_pattern)

    fixed_start_dt = datetime.strptime(fixed_start, date_pattern)
    fixed_end_dt = datetime.strptime(fixed_end, date_pattern)

    return (
        event_start_dt >= fixed_start_dt
        and event_end_dt <= fixed_end_dt
    )

def extract_photo_urls(event):
    """
    Obtain photo URLs for all photos of each event.
    If there's multiple photo URLs, they are separated by
    a comma delimiter

    Input : list
    Output : string
    """
    if 'photos' in event:
        photo_urls = list(map(lambda photo: photo['photo']['url'], event['photos']))
        photo_urls_string = ",".join(photo_urls)
        return photo_urls_string if len(photo_urls_string) > 0 else dataframe.NA_VALUE
    return dataframe.NA_VALUE

def map_country_code_to_country_name(d_countries, country_code):
    """
    Returns the country name associated with the provided country code
    based on the countries dictionary of { country code : country name }
    If country code does not exist, return NA

    Input : dictionary, string
    Output : string 
    """
    if country_code in d_countries:
        return d_countries[country_code]
    return dataframe.NA_VALUE


def max_score_for_rating(restaurants_df, rating_text):
    """
    Returns the maximum score recorded for a rating text
    across all records 

    Input : dataframe, string
    Output : float
    """

    # Store ratings_text_score as : (rating_text, aggregate_rating_score)
    rating_text_score = zip(
        restaurants_df[dataframe.RATING_TEXT],
        restaurants_df[dataframe.USER_AGGREGATE_RATING]
    )

    all_ratings = list(filter(lambda text_score: text_score[0] == rating_text, rating_text_score))
    rating_text_agg_scores = list(map(lambda text_score: text_score[1], all_ratings))
    return max(rating_text_agg_scores)

def min_score_for_rating(restaurants_df, rating_text):
    """
    Returns the minimum score recorded for a rating text
    across all records 

    Input : dataframe, string
    Output : float
    """

    # Store ratings_text_score as : (rating_text, aggregate_rating_score)
    rating_text_score = zip(
        restaurants_df[dataframe.RATING_TEXT],
        restaurants_df[dataframe.USER_AGGREGATE_RATING]
    )

    all_ratings = list(filter(lambda text_score: text_score[0] == rating_text, rating_text_score))
    rating_text_agg_scores = list(map(lambda text_score: text_score[1], all_ratings))
    return min(rating_text_agg_scores)
