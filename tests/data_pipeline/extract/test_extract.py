"""
Tests for data_pipeline's extract functions
"""
from tests.data_pipeline.extract.mocks import (
    mock_one_extract_restaurant_records_from_parsed_json,
    mock_two_extract_restaurant_records_from_parsed_json,
    mock_one_df_extract_countries_data,
    mock_one_df_expected_extract_countries_data,
    mock_two_df_extract_countries_data,
    mock_two_df_expected_extract_countries_data
)

from data_pipeline import extract

def test_extract_restaurant_records_from_parsed_json():
    """
    Test that extract_restaurant_records_from_parsed_json()
    obtains all restaurant data and collects them into a list
    """

    # Check that fn returns an empty list if there's no
    # restaurants data
    mock_one = extract.extract_restaurant_records_from_parsed_json(
        mock_one_extract_restaurant_records_from_parsed_json
    )
    assert not mock_one

    # Check that fn returns a list with all restaurant data present
    # if there's restaurant data provided
    mock_two = extract.extract_restaurant_records_from_parsed_json(
        mock_two_extract_restaurant_records_from_parsed_json
    )
    assert len(mock_two) == 4

def test_extract_countries_data():
    """
    Test that test_extract_countries_data()
    creates a dictionary mapping of { country code : country name }
    given an input country code dataframe 
    """

    # Check that a dictionary mapping of { country code : country name } is
    # created when there's input data
    d_countries_one = extract.extract_countries_data(mock_one_df_extract_countries_data)
    assert d_countries_one == mock_one_df_expected_extract_countries_data

    # Check that an empty dictionary mapping is returned if input data is an empty
    # dataframe
    d_countries_two = extract.extract_countries_data(mock_two_df_extract_countries_data)
    assert d_countries_two == mock_two_df_expected_extract_countries_data
