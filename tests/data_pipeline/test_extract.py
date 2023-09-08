"""
Tests for data_pipeline's extract functions
"""
from data_pipeline.extract import extract_restaurants_data

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
