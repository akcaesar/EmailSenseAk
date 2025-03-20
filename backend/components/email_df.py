"""
Author: Akshay NS
Script for creating a Pandas DataFrame from the emails, and cleaning it. 

"""

import pandas as pd
from .login import fetch_emails
import os
from bs4 import BeautifulSoup
import html2text
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
import nltk
nltk.download('punkt_tab')



emails = fetch_emails()
email_df = pd.DataFrame(emails)
email_df_mod = email_df.copy()


# # Save the pandas DataFrame to a CSV file in a folder
# output_folder = "/workspaces/codespaces-blank/EmailSense_cp/backend/data"
# output_file = f"{output_folder}/email_data.csv"

# # Ensure the folder exists
# os.makedirs(output_folder, exist_ok=True)

# # Save the DataFrame
# email_df_mod.to_csv(output_file, index=False)
# print(f"DataFrame saved to {output_file}")


##cleaning the text
htmlremtext = html2text.HTML2Text()
htmlremtext.ignore_links = True
htmlremtext.bypass_tables = False
def clean_text(text):
    if text:
        soup = BeautifulSoup(text, 'html.parser')
        text = soup.get_text()
        cleantext = "\n".join(line.strip() for line in text.splitlines() if line.strip())
        cleantext = htmlremtext.handle(cleantext)
        return cleantext
    return text

email_df_mod['Body'] = email_df_mod['Body'].apply(clean_text)



####summary of the email
# Function to summarize text
def summarize_text(text, sentences_count=3):
    if not text or not isinstance(text, str):
        return ""  # Return empty string for invalid or empty input
    try:
        # Parse the input text
        parser = PlaintextParser.from_string(text, Tokenizer("english"))
        # Create an LSA summarizer
        summarizer = LsaSummarizer()
        # Generate the summary
        summary = summarizer(parser.document, sentences_count=sentences_count)
        # Combine the summary sentences into a single string
        return " ".join(str(sentence) for sentence in summary)
    except Exception as e:
        print(f"Error summarizing text: {e}")
        return ""

email_df_mod['Body'] = email_df_mod['Body'].apply(lambda x: summarize_text(x, sentences_count=5))

