"""
This file contains the output values to print to terminal for Q3
"""
import pandas as pd

PARA_ONE = '''
According to the dataset, it seems that rating categories (apart from the ones mentioned in Q3)
are in other languages (apart from "Not rated"). Hence, I assume that the ratings mentioned in Q3
form a complete, continuous (increasing) scale, from lowest score to highest score :
    1) Poor (lowest score)
    2) Average
    3) Good
    4) Very Good
    5) Excellent

To determine the ranges for each rating, with just the given dataset alone,
I have decided to find the minimum and maximum score associated with each rating 
within the dataset records. I have collected them into a table as show below:
'''

PARA_TWO = '''
1. Determining the minimum and maximum possible score for the entire scale
With the assumption that "Poor" is the category for the lowest score, the minimum score for
"Poor" would be 0 (since most rating scales start from 0.0). 

With the assumption that "Excellent" is the category for the highest score,
the maximum score for "Excellent" would be the maximum score available in the scale. Since the 
scores observed range from 2.2 to 4.9, this suggests that the rating is based on a scale of score
0 to 5. Hence the maximum score for "Excellent" would be 5.0.

2. Determining the minimum and maximum possible score for each rating category
With the assumption that the ratings form a complete, continuous (increasing) scale
(established in the first paragraph), the minimum score for each category would be
one point away from the maximum score for the previous category. Similarly, the maximum 
score for each category would be one point away from the minimum score for the next category.
(With the exception of the minimium score for "Poor" being 0.0 and maximum score for "Excellent" 
being 5.0, as established in the previous paragraph). 

3. Based on points 1 and 2, these are the thresholds that I have established for the different
rating texts
'''

data_thresholds = {
    "Minimum Rating Score": [
        0.0,
        2.5,
        3.5,
        4.0,
        4.5
    ],
    "Maximum Rating Score" : [
        2.4,
        3.4,
        3.9,
        4.4,
        5.0
    ]
}

df_index_thresholds = [
    "Poor",
    "Average",
    "Good",
    "Very Good",
    "Excellent"
]

# Creates pandas DataFrame.
DF_Q3_THRESHOLDS = pd.DataFrame(data_thresholds, index=df_index_thresholds)
