"""
Tests for data_pipeline's extract functions
"""
from mocks import (
    mock_one_extract_restaurant_records_from_parsed_json,
    mock_two_extract_restaurant_records_from_parsed_json
)

from data_pipeline.extract import (
    extract_restaurants_data,
    extract_restaurant_records_from_parsed_json
)

def test_extract_restaurants_data():
    """
    Test that extract_restaurants_data()
    returns a list of (valid) restaurant data records
    """
    data = extract_restaurants_data()

    # Data should not be None
    assert data is not None

    # Data should be a list with records
    assert isinstance(data, list)
    assert len(data) != 0

    # Check that the expected key values are present
    for item in data:
        assert "results_found" in item
        assert "results_start" in item
        assert "results_shown" in item
        assert "restaurants" in item

def test_extract_restaurant_records_from_parsed_json():
    """
    Test that extract_restaurant_records_from_parsed_json()
    obtains all restaurant data and collects them into a list
    """

    # Check that fn returns an empty list if there's no
    # restaurants data
    mock_one = extract_restaurant_records_from_parsed_json(
        mock_one_extract_restaurant_records_from_parsed_json
    )
    assert not mock_one

    # Check that fn returns a list with all restaurant data present
    # if there's restaurant data provided
    mock_two = extract_restaurant_records_from_parsed_json(
        mock_two_extract_restaurant_records_from_parsed_json
    )
    assert len(mock_two) == 4
    