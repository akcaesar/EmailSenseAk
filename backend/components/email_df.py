"""
Author: Akshay NS
Script for creating a Pandas DataFrame from the emails, and cleaning it. 

"""

import pandas as pd
from .login import fetch_emails


emails = fetch_emails()
email_df = pd.DataFrame(emails)
email_df_mod = email_df.copy()

# Convert the 'Date' column to datetime
# email_df_mod['Date'] = pd.to_datetime(email_df_mod['Date'], format='%a, %d %b %Y %H:%M:%S %z')

# Extract date, time, and day
# email_df_mod['date'] = email_df_mod['Date'].dt.date
# email_df_mod['time'] = email_df_mod['Date'].dt.time
# email_df_mod['day'] = email_df_mod['Date'].dt.day_name()

# # Drop the original 'Date' column if no longer needed
# email_df_mod = email_df_mod.drop(columns=['Date'])





