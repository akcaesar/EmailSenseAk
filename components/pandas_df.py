"""
Author: Akshay NS
Script for creating a Pandas DataFrame from the emails, and cleaning it. 

"""

import pandas as pd
from .login import fetch_emails


emails = fetch_emails()
email_df = pd.DataFrame(emails)

# if __name__ == "__main__":
#     df = pd.DataFrame(emails)
    


