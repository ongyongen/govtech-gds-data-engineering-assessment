"""
Tests for data_pipeline's extract functions
"""
from tests.data_pipeline.mocks import (
    mock_one_extract_restaurant_records_from_parsed_json,
    mock_two_extract_restaurant_records_from_parsed_json,
    mock_one_df_extract_countries_data,
    mock_one_df_expected_extract_countries_data,
    mock_two_df_extract_countries_data,
    mock_two_df_expected_extract_countries_data
)

from data_pipeline import extract

def test_extract_restaurants_data():
    """
    Test that extract_restaurants_data()
    returns a list of (valid) restaurant data records
    """
    data = extract.extract_restaurants_data()

    # Data should not be None
    assert data is not None

    # Data should be a list with records
    assert isinstance(data, list)
    assert len(data) != 0

    # Check that the expected key values are present
    # and have the expected data type
    for item in data:
        assert "results_found" in item
        assert isinstance(data[0]["results_found"], int)

        assert "results_start" in item
        assert isinstance(data[0]["results_start"], int)

        assert "results_shown" in item
        assert isinstance(data[0]["results_shown"], int)

        assert "restaurants" in item
        assert isinstance(data[0]["restaurants"], list)


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
