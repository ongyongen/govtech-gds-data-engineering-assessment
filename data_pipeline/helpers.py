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
