"""
Tests for data_pipeline's transform functions
"""
from data_pipeline import transform
from tests.data_pipeline.transform.mocks import (
    mock_d_countries_test_process_restaurants,
    mock_restaurants_list_test_process_restaurants,
    mock_expected_df_test_process_restaurants,
    mock_df_prepare_data_for_q1,
    mock_expected_df_prepare_data_for_q1,
    mock_df_process_restaurant_events_within_date_range,
    mock_expected_df_process_restaurant_events_within_date_range
)

def test_process_restaurants():
    """
    Test that restaurant data (from a list) is collected
    into a dataframe for subsequent data processing steps
    """

    test_df = transform.process_restaurants(
        mock_d_countries_test_process_restaurants,
        mock_restaurants_list_test_process_restaurants
    )
    # Check that a dataframe object is returned
    assert isinstance(test_df, object)

    # Check that a dataframe object which is expected to have 1 entry
    # does indeed have 1 entry
    assert len(test_df) == 1

    # Check that all required columns are present and values for the
    # respective data fields are correct
    for i in range(len(mock_expected_df_test_process_restaurants)):
        for column in mock_expected_df_prepare_data_for_q1.columns:
            assert test_df.loc[i, column] == \
                mock_expected_df_test_process_restaurants.loc[i, column]

def test_prepare_data_for_q1():
    """
    Test that restaurant dataframe is cleaned and ready for 
    export to csv
    """

    test_df = transform.prepare_data_for_q1(mock_df_prepare_data_for_q1)
    # Check that a dataframe object is returned
    assert isinstance(test_df, object)

    # Check that a dataframe object which is expected to have 1 entry
    # does indeed have 1 entry
    assert len(test_df) == 1

    # Check that only the relevant columns required for Q1 are extracted
    assert sorted(test_df) == sorted(mock_expected_df_prepare_data_for_q1.columns)

    # Check that all required columns are present and values for the
    # respective data fields are correct
    for i in range(len(mock_expected_df_prepare_data_for_q1)):
        for column in mock_expected_df_prepare_data_for_q1.columns:
            assert test_df.loc[i, column] == \
                mock_expected_df_prepare_data_for_q1.loc[i, column]

def test_process_restaurant_events_within_date_range():
    """
    Test that events data for each restaurant is 
    extracted into a dataframe
    """

    test_df = transform.process_restaurant_events_within_date_range(
        mock_df_process_restaurant_events_within_date_range,
        "2019-03-01",
        "2019-03-30"
    )
    # Check that a dataframe object is returned
    assert isinstance(test_df, object)

    # Check that a dataframe object which is expected to have 2 entries
    # does indeed have 2 entries
    assert len(test_df) == 2

    # Check that only the relevant columns required for Q1 are extracted
    assert sorted(test_df) == \
        sorted(mock_expected_df_process_restaurant_events_within_date_range.columns)

    # Check that all required columns are present and values for the
    # respective data fields are correct
    for i in range(len(mock_expected_df_process_restaurant_events_within_date_range)):
        for column in mock_expected_df_process_restaurant_events_within_date_range.columns:
            assert test_df.loc[i, column] == \
                mock_expected_df_process_restaurant_events_within_date_range.loc[i, column]
