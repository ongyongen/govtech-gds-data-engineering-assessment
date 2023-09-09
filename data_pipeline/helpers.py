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
