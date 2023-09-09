"""
Tests for data_pipeline's extract functions
"""

from data_pipeline import helpers
from constants import dataframe
from tests.data_pipeline.helpers.mocks import (
    mock_one_replace_na_cells,
    mock_two_replace_na_cells
)

def test_create_template_restaurants_df():
    """
    Test that test_create_template_restaurants_df()
    returns a template dataframe with expected columns
    present
    """

    # Check that all expected columns are present
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

def test_create_template_events_df():
    """
    Test that create_template_events_df()
    returns a template dataframe with expected columns
    present
    """

    # Check that all expected columns are present
    test_df = helpers.create_template_events_df()
    assert dataframe.EVENT_ID in test_df
    assert dataframe.RESTAURANT_ID in test_df
    assert dataframe.RESTAURANT_NAME in test_df
    assert dataframe.PHOTO_URL in test_df
    assert dataframe.EVENT_TITLE in test_df
    assert dataframe.EVENT_START_DATE in test_df
    assert dataframe.EVENT_END_DATE in test_df


def test_replace_na_cells():
    """
    Test that replace_na_cells()
    returns a template dataframe with empty cells
    replaced by an expected replacement string
    present
    """

    # Check that empty (None) cells are replaced by NA
    test_df_one = helpers.replace_na_cells(mock_one_replace_na_cells, "NA")
    assert test_df_one.loc[0,"A"] == "NA"
    assert test_df_one.loc[0,"B"] == "NA"

    # Check that empty (None) cells are replaced by 0
    test_df_two = helpers.replace_na_cells(mock_two_replace_na_cells, 0)
    assert test_df_two.loc[0,"C"] == 0
    assert test_df_two.loc[0,"D"] == 0
