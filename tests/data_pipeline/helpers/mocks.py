"""
This file contains mock data for data pipeline - helpers' function's
testing 
"""
import pandas as pd

# Mock data for : replace_na_cells
mock_one_replace_na_cells = pd.DataFrame(columns=["A","B"])
mock_one_replace_na_cells.loc[0,"A"] = None
mock_one_replace_na_cells.loc[0,"B"] = None

mock_two_replace_na_cells = pd.DataFrame(columns=["C","D"])
mock_two_replace_na_cells.loc[0,"C"] = None
mock_two_replace_na_cells.loc[0,"D"] = None

# Mock data for : extract_photo_urls
mock_one_extract_photo_urls = {
    "photos": []
}

mock_two_extract_photo_urls = {
    "photos": [
        {"photo": {'url': "1"}},
        {"photo": {'url': "2"}},
        {"photo": {'url': "3"}}
    ]
}

mock_three_extract_photo_urls = {
    "photos": [
        {"photo": {'url': "1"}}
    ]
}
