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

# Mock data for : test_prepare_data_for_q1
mock_data_prepare_data_for_q1 = [
    {
      dataframe.RESTAURANT_ID: 18649486.0,
      dataframe.RESTAURANT_NAME: "The Drunken Botanist",
      dataframe.COUNTRY_ID: None,
      dataframe.CITY: "Gurgaon",
      dataframe.USER_RATING_VOTES: None,
      dataframe.USER_AGGREGATE_RATING: "4.4",
      dataframe.CUISINES: "Continental, Italian, North Indian, Chinese",
      dataframe.RATING_TEXT: "Very Good",
      dataframe.COUNTRY: "India",
      dataframe.EVENTS: None,
    }
]

mock_df_prepare_data_for_q1 = pd.DataFrame(
    mock_data_prepare_data_for_q1
)

mock_expected_data_prepare_data_for_q1 = [
    {
      dataframe.RESTAURANT_ID: 18649486.0,
      dataframe.RESTAURANT_NAME: "The Drunken Botanist",
      dataframe.COUNTRY: "India",
      dataframe.CITY: "Gurgaon",
      dataframe.USER_RATING_VOTES: dataframe.NA_VALUE,
      dataframe.USER_AGGREGATE_RATING: "4.4",
      dataframe.CUISINES: "Continental, Italian, North Indian, Chinese",
    }
]

mock_expected_df_prepare_data_for_q1 = pd.DataFrame(
    mock_expected_data_prepare_data_for_q1
)

# Mock data for : test_process_restaurant_events_within_date_range
mock_events_list_test_process_restaurant_events_within_date_range = [
    {
      dataframe.RESTAURANT_ID: 18649486.0,
      dataframe.RESTAURANT_NAME: "The Drunken Botanist",
      dataframe.COUNTRY_ID: 1,
      dataframe.CITY: "Gurgaon",
      dataframe.USER_RATING_VOTES: None,
      dataframe.USER_AGGREGATE_RATING: "4.4",
      dataframe.CUISINES: "Continental, Italian, North Indian, Chinese",
      dataframe.RATING_TEXT: "Very Good",
      dataframe.COUNTRY: "India",
      dataframe.EVENTS: [
          {
          "event": {
            "event_id": 322331,
            "title": "Test Title 1",
            "friendly_start_date": "06 March",
            "friendly_end_date": "07 March",
            "friendly_timing_str": "Wednesday, 6th March - Wednesday, 28th August",
            "start_date": "2019-03-06",
            "end_date": "2019-03-07",
            "end_time": "23:59:59",
            "start_time": "20:00:00",
            "is_active": 1,
            "date_added": "2019-03-06 11:41:21",
            "photos": [
              {
                "photo": {
                  "url": "1",
                  "thumb_url": "example",
                  "order": 0,
                  "md5sum": "ac34cf3c271c9052e9d248c243df65a1",
                  "id": 434436,
                  "photo_id": 434436,
                  "uuid": 52695233531,
                  "type": "FEATURED"
                }
              },
              {
                "photo": {
                  "url": "2",
                  "thumb_url": "example",
                  "order": 0,
                  "md5sum": "ac34cf3c271c9052e9d248c243df65a1",
                  "id": 434436,
                  "photo_id": 434436,
                  "uuid": 52695233531,
                  "type": "FEATURED"
                }
              }
            ],
          }
        }
      ],
    },
    {
      dataframe.RESTAURANT_ID: 34831785.0,
      dataframe.RESTAURANT_NAME: "Cafeteria & Co",
      dataframe.COUNTRY_ID: 1,
      dataframe.CITY: "New Delhi",
      dataframe.USER_RATING_VOTES: None,
      dataframe.USER_AGGREGATE_RATING: "4.4",
      dataframe.CUISINES: "English",
      dataframe.RATING_TEXT: "Good",
      dataframe.COUNTRY: "India",
      dataframe.EVENTS: [
          {
          "event": {
            "event_id": 400300,
            "title": "Test Title 2",
            "friendly_start_date": "01 March",
            "friendly_end_date": "30 March",
            "friendly_timing_str": "Wednesday, 6th March - Wednesday, 28th August",
            "start_date": "2019-03-01",
            "end_date": "2019-03-30",
            "end_time": "23:59:59",
            "start_time": "20:00:00",
            "is_active": 1,
            "date_added": "2019-03-06 11:41:21",
            "photos": [],
          }
        }
      ],
    },
]

mock_df_process_restaurant_events_within_date_range = pd.DataFrame(
    mock_events_list_test_process_restaurant_events_within_date_range
)

mock_expected_data_process_restaurant_events_within_date_range = [
    {
      dataframe.EVENT_ID: 322331,
      dataframe.RESTAURANT_ID: 18649486.0,
      dataframe.RESTAURANT_NAME: "The Drunken Botanist",
      dataframe.PHOTO_URL: "1,2",
      dataframe.EVENT_TITLE: "Test Title 1",
      dataframe.EVENT_START_DATE: "2019-03-06",
      dataframe.EVENT_END_DATE: "2019-03-07"
    },
    {
      dataframe.EVENT_ID: 400300,
      dataframe.RESTAURANT_ID: 34831785,
      dataframe.RESTAURANT_NAME: "Cafeteria & Co",
      dataframe.PHOTO_URL: "NA",
      dataframe.EVENT_TITLE: "Test Title 2",
      dataframe.EVENT_START_DATE: "2019-03-01",
      dataframe.EVENT_END_DATE: "2019-03-30"
    }
]

mock_expected_df_process_restaurant_events_within_date_range = pd.DataFrame(
    mock_expected_data_process_restaurant_events_within_date_range
)

# Mock data for : prepare_data_for_q2
mock_data_prepare_data_for_q2 = [
    {
      dataframe.EVENT_ID: 322331,
      dataframe.RESTAURANT_ID: 18649486.0,
      dataframe.RESTAURANT_NAME: None,
      dataframe.PHOTO_URL: "1,2",
      dataframe.EVENT_TITLE: "Test Title 1",
      dataframe.EVENT_START_DATE: "2019-03-06",
      dataframe.EVENT_END_DATE: "2019-03-07"
    },
    {
      dataframe.EVENT_ID: 400300,
      dataframe.RESTAURANT_ID: 34831785,
      dataframe.RESTAURANT_NAME: "Cafeteria & Co",
      dataframe.PHOTO_URL: "NA",
      dataframe.EVENT_TITLE: None,
      dataframe.EVENT_START_DATE: "2019-03-01",
      dataframe.EVENT_END_DATE: "2019-03-30"
    }
]

mock_df_prepare_data_for_q2 = pd.DataFrame(
    mock_data_prepare_data_for_q2
)

mock_expected_data_prepare_data_for_q2 = [
    {
      dataframe.EVENT_ID: 322331,
      dataframe.RESTAURANT_ID: 18649486.0,
      dataframe.RESTAURANT_NAME: dataframe.NA_VALUE,
      dataframe.PHOTO_URL: "1,2",
      dataframe.EVENT_TITLE: "Test Title 1",
      dataframe.EVENT_START_DATE: "2019-03-06",
      dataframe.EVENT_END_DATE: "2019-03-07"
    },
    {
      dataframe.EVENT_ID: 400300,
      dataframe.RESTAURANT_ID: 34831785,
      dataframe.RESTAURANT_NAME: "Cafeteria & Co",
      dataframe.PHOTO_URL: dataframe.NA_VALUE,
      dataframe.EVENT_TITLE: dataframe.NA_VALUE,
      dataframe.EVENT_START_DATE: "2019-03-01",
      dataframe.EVENT_END_DATE: "2019-03-30"
    }
]

mock_expected_df_prepare_data_for_q2 = pd.DataFrame(
    mock_expected_data_prepare_data_for_q2
)
