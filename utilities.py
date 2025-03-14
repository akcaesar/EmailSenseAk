"""
Author: Akshay NS

Contains utility functions which can be performed on the dataframes.

"""

import pandas as pd

def get_emails_count(df: pd.DataFrame) -> int:
    return len(df)