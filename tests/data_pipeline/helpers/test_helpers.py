"""
Tests for data_pipeline's extract functions
"""

from data_pipeline import helpers
from constants import dataframe

def test_create_template_restaurants_df():
    """
    Test that test_create_template_restaurants_df()
    returns a template dataframe with expected columns
    present
    """

    test_df = helpers.create_template_restaurants_df()
    assert dataframe.RESTAURANT_ID in test_df
    assert dataframe.RESTAURANT_NAME in test_df
    assert dataframe.COUNTRY in test_df
    assert dataframe.CITY in test_df
    assert dataframe.USER_RATING_VOTES in test_df
    assert dataframe.CUISINES in test_df
    assert dataframe.USER_AGGREGATE_RATING in test_df
    assert dataframe.COUNTRY_ID in test_df
    assert dataframe.RATING_TEXT in test_df
    assert dataframe.PHOTO_URL in test_df
    assert dataframe.EVENTS in test_df
    assert dataframe.EVENT_ID in test_df
    assert dataframe.EVENT_TITLE in test_df
    assert dataframe.EVENT_START_DATE in test_df
    assert dataframe.EVENT_END_DATE in test_df
