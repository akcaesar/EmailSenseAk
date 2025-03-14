"""
Author: Akshay NS
This script processes the emails fetched from the user's Gmail inbox.
It creates a pandas DataFrame from the emails data and returns it.

"""

import pandas as pd
from login import fetch_emails

def create_dataframe(emails):
    df = pd.DataFrame(emails)
    return df

if __name__ == "__main__":
    emails = fetch_emails()
    df = create_dataframe(emails)
    print(df)