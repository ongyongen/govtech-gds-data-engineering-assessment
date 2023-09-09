"""
This file contains mock data for data pipeline - transform's function's
testing 
"""

import pandas as pd
from constants import dataframe

# Mock data for : test_process_restaurants
mock_d_countries_test_process_restaurants = {
    1 : "India",
    14 : "Australia",
    30 : "Brazil"
}

mock_df_columns_test_process_restaurants = [
       dataframe.RESTAURANT_ID,
       dataframe.RESTAURANT_NAME,
       dataframe.COUNTRY_ID,
       dataframe.CITY,
       dataframe.USER_RATING_VOTES,
       dataframe.USER_AGGREGATE_RATING,
       dataframe.CUISINES,
       dataframe.RATING_TEXT,
       dataframe.COUNTRY,
       dataframe.EVENTS
]

mock_restaurants_list_test_process_restaurants = [
    {
        "restaurant": {
          "R": {
            "res_id": 18649486
          },
          "apikey": "cba15beb4c265876a9828f242b4cf41c",
          "id": "18649486",
          "name": "The Drunken Botanist",
          "url": "test",
          "location": {
            "address": "test",
            "locality": "Cyber Hub, DLF Cyber City",
            "city": "Gurgaon",
            "city_id": 1,
            "latitude": "28.4936741035",
            "longitude": "77.0883342996",
            "zipcode": "",
            "country_id": 1,
            "locality_verbose": "Cyber Hub, DLF Cyber City, Gurgaon"
          },
          "switch_to_order_menu": 0,
          "cuisines": "Continental, Italian, North Indian, Chinese",
          "average_cost_for_two": 1500,
          "price_range": 3,
          "currency": "Rs.",
          "offers": [],
          "zomato_events": [],
          "opentable_support": 0,
          "is_zomato_book_res": 0,
          "mezzo_provider": "OTHER",
          "is_book_form_web_view": 0,
          "book_form_web_view_url": "",
          "book_again_url": "",
          "thumb": "test",
          "user_rating": {
            "aggregate_rating": "4.4",
            "rating_text": "Very Good",
            "rating_color": "5BA829",
            "votes": "4765",
            "has_fake_reviews": 0
          },
          "photos_url": "test",
          "menu_url": "test",
          "featured_image": "test",
          "has_online_delivery": 0,
          "is_delivering_now": 0,
          "has_fake_reviews": 0,
          "include_bogo_offers": True,
          "deeplink": "zomato://restaurant/18649486",
          "is_table_reservation_supported": 0,
          "has_table_booking": 0,
          "events_url": "test",
          "establishment_types": []
        }
    }
]

mock_expected_df_list_test_process_restaurants = pd.DataFrame(columns=[
    dataframe.RESTAURANT_ID,
    dataframe.RESTAURANT_NAME,
    dataframe.COUNTRY_ID,
    dataframe.CITY,
    dataframe.USER_RATING_VOTES,
    dataframe.USER_AGGREGATE_RATING,
    dataframe.CUISINES,
    dataframe.RATING_TEXT,
    dataframe.COUNTRY,
    dataframe.EVENTS
])


mock_expected_data_test_process_restaurants = [
    {
      dataframe.RESTAURANT_ID: 18649486.0,
      dataframe.RESTAURANT_NAME: "The Drunken Botanist",
      dataframe.COUNTRY_ID: 1,
      dataframe.CITY: "Gurgaon",
      dataframe.USER_RATING_VOTES: "4765",
      dataframe.USER_AGGREGATE_RATING: "4.4",
      dataframe.CUISINES: "Continental, Italian, North Indian, Chinese",
      dataframe.RATING_TEXT: "Very Good",
      dataframe.COUNTRY: "India",
      dataframe.EVENTS: [],
    }
]

mock_expected_df_test_process_restaurants = pd.DataFrame(
    mock_expected_data_test_process_restaurants
)
