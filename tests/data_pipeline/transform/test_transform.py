"""
Tests for data_pipeline's transform functions
"""
from data_pipeline import transform
from tests.data_pipeline.transform.mocks import (
    mock_d_countries_test_process_restaurants,
    mock_restaurants_list_test_process_restaurants,
    mock_df_columns_test_process_restaurants,
    mock_expected_df_test_process_restaurants
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
    for column in mock_df_columns_test_process_restaurants:
        assert column in test_df
        assert test_df.loc[0, column] == \
            mock_expected_df_test_process_restaurants.loc[0, column]
