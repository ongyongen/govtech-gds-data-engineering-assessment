"""
This file contains mock data for data pipeline - helpers' function's
testing 
"""
import pandas as pd

mock_one_replace_na_cells = pd.DataFrame(columns=["A","B"])
mock_one_replace_na_cells.loc[0,"A"] = None
mock_one_replace_na_cells.loc[0,"B"] = None

mock_two_replace_na_cells = pd.DataFrame(columns=["C","D"])
mock_two_replace_na_cells.loc[0,"C"] = None
mock_two_replace_na_cells.loc[0,"D"] = None
