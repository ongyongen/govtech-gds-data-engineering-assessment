"""
This file contains methods used in the Extract phase of the ETL data pipeline
"""

import requests
from constants import urls

def extract_restaurants_data():
    """
    GET restaurant data from the url link provided

    Input : None
    Output : Object
    """
    url = urls.RESTAURANTS_DATA_URL

    try:
        response = requests.get(url, timeout=20)

        if response.status_code == 200:
            return response.json()
        print(f"API failed with status code {response.status_code}")
        print(f"Error: {response.text}")
        return None

    except requests.exceptions.Timeout:
        print("Error: request to API timed out")
        return None
