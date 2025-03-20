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
import re



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


# Function to clean text
def preprocess_text(text):
    if not text or not isinstance(text, str):
        return ""
    
    # Remove URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    
    # Remove excessive whitespace and repetitive patterns
    text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces/newlines with a single space
    text = re.sub(r'(.)\1{4,}', r'\1', text)  # Remove repetitive characters (e.g., "-----" -> "-")
    
    # Remove HTML tags
    soup = BeautifulSoup(text, "html.parser")
    text = soup.get_text()
    
    return text.strip()

# Function to summarize text
def summarize_text(text, sentences_count=3):
    if not text or not isinstance(text, str):
        return ""
    try:
        # Parse the cleaned text
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

email_df_mod['Summarized'] = email_df_mod['Body']
email_df_mod['Summarized'] = email_df_mod['Body'].apply(preprocess_text)
email_df_mod['Summarized'] = email_df_mod['Body'].apply(summarize_text)