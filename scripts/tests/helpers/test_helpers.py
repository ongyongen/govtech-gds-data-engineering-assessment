"""
Tests for data_pipeline's extract functions
"""

from data_pipeline import helpers
from constants import dataframe

from .mocks import (
    mock_one_replace_na_cells,
    mock_two_replace_na_cells,
    mock_one_extract_photo_urls,
    mock_two_extract_photo_urls,
    mock_three_extract_photo_urls,
    mock_d_countries_map_country_code_to_country_name,
    mock_df_test_scores_for_rating
)

def test_create_template_restaurants_df():
    """
    Test that test_create_template_restaurants_df
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
    Test that create_template_events_df
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
    Test that replace_na_cells
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

def test_event_occurs_within_dates():
    """
    Test that event_occurs_within_dates
    returns true if event occurs in a stated
    date range (false otherwise)
    """

    # Check that true is returned when
    # an event falls within the stated date range
    test_one = helpers.event_occurs_within_dates(
        "2019-04-03",
        "2019-04-03",
        "2019-04-03",
        "2019-04-03",
    )
    assert test_one

    # Check that false is returned when
    # an event falls outside the stated date range
    test_two = helpers.event_occurs_within_dates(
        "2019-04-03",
        "2019-04-10",
        "2019-04-01",
        "2019-04-02",
    )
    assert not test_two

def test_extract_photo_urls():
    """
    Test that extract_photo_urls returns
    a comma-delimited string containing all
    photo urls if there's photo urls. Else return 
    the replacement string for empty dataframes
    """

    # Check that the empty replacement string for the dataframe is
    # returned if there are no photos
    test_one = helpers.extract_photo_urls(mock_one_extract_photo_urls)
    assert test_one == dataframe.NA_VALUE

    # Check that the photo urls string (containing all photos url)
    # is returned if there are multiple photos
    test_two = helpers.extract_photo_urls(mock_two_extract_photo_urls)
    assert test_two == "1,2,3"

    # Check that the photo urls string (containing all photos url)
    # is returned if there is 1 photo
    test_three = helpers.extract_photo_urls(mock_three_extract_photo_urls)
    assert test_three == "1"

def test_map_country_code_to_country_name():
    """
    Test that test_map_country_code_to_country_name returns
    name of the country in countries dictionary given a country code
    """

    # Check that country name is returned if there is a country code
    test_one = helpers.map_country_code_to_country_name(
        mock_d_countries_map_country_code_to_country_name,
        1
    )
    assert test_one == "Singapore"

    # Check that placeholder NA value is returned if
    # there is no associated country name for the input country code
    test_one = helpers.map_country_code_to_country_name(
        mock_d_countries_map_country_code_to_country_name,
        10
    )
    assert test_one == dataframe.NA_VALUE

def test_max_score_for_rating():
    """
    Test that test_max_score_for_rating returns
    the maximum score for a rating text
    """

    test_max_poor = helpers.max_score_for_rating(
        mock_df_test_scores_for_rating,
        dataframe.POOR
    )

    test_max_average = helpers.max_score_for_rating(
        mock_df_test_scores_for_rating,
        dataframe.AVERAGE
    )

    test_max_good = helpers.max_score_for_rating(
        mock_df_test_scores_for_rating,
        dataframe.GOOD
    )

    test_max_very_good = helpers.max_score_for_rating(
        mock_df_test_scores_for_rating,
        dataframe.VERY_GOOD
    )

    test_max_excellent = helpers.max_score_for_rating(
        mock_df_test_scores_for_rating,
        dataframe.EXCELLENT
    )

    assert test_max_poor == "2.4"
    assert test_max_average == "3.5"
    assert test_max_good == "4.0"
    assert test_max_very_good == "4.4"
    assert test_max_excellent == "4.9"


def test_min_score_for_rating():
    """
    Test that test_min_score_for_rating returns
    the minimum score for a rating text
    """

    test_min_poor = helpers.min_score_for_rating(
        mock_df_test_scores_for_rating,
        dataframe.POOR
    )

    test_min_average = helpers.min_score_for_rating(
        mock_df_test_scores_for_rating,
        dataframe.AVERAGE
    )

    test_min_good = helpers.min_score_for_rating(
        mock_df_test_scores_for_rating,
        dataframe.GOOD
    )

    test_min_very_good = helpers.min_score_for_rating(
        mock_df_test_scores_for_rating,
        dataframe.VERY_GOOD
    )

    test_min_excellent = helpers.min_score_for_rating(
        mock_df_test_scores_for_rating,
        dataframe.EXCELLENT
    )

    assert test_min_poor == "2.0"
    assert test_min_average == "3.5"
    assert test_min_good == "4.0"
    assert test_min_very_good == "4.4"
    assert test_min_excellent == "4.7"
