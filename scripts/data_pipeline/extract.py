"""
This file contains methods used in the Extract phase of the ETL data pipeline
"""

import requests
from constants import dataframe, paths

def extract_restaurants_data():
    """
    GET restaurant data from the url link provided

    Input : None
    Output : Object
    """
    url = paths.RESTAURANTS_DATA_URL

    try:
        response = requests.get(url, timeout=20)

        # Successfully retrieved data
        if response.status_code == 200:
            return response.json()

        # Did not successfully retrieve data
        print(f"API failed with status code {response.status_code}")
        print(f"Error: {response.text}")
        return None
    # Connection timeout
    except requests.exceptions.Timeout:
        print("Error: request to API timed out")
        return None

def extract_restaurant_records_from_parsed_json(data):
    """
    Extract data for each restaurant from the JSON file and 
    collect them into a single list for ease of further processing

    Input : list
    Output : list
    """

    restaurant_records = []
    for record in data:
        total_records = record['results_shown']
        if total_records > 0:
            restaurant_records += record['restaurants']
    return restaurant_records

def extract_countries_data(countries):
    """
    Create a dictionary to store key-value of pairs of
    { country code : country name } mapping

    Input : dataframe
    Output : dictionary
    """

    d_countries = {}
    for index in range(len(countries)):
        country_name = countries.loc[index, dataframe.COUNTRY]
        country_code = countries.loc[index, dataframe.COUNTRY_CODE]
        d_countries[country_code] = country_name
    return d_countries
