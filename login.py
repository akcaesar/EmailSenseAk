import imaplib
import email
import os
from dotenv import load_dotenv

load_dotenv()


def fetch_emails():
    EMAIL = os.getenv('EMAIL_USER')
    APP_PASSWORD = os.getenv('EMAIL_PASSWORD')

    if not EMAIL or not APP_PASSWORD:
        print("Error: Missing environment variables for email credentials.")
        exit(1)

    # Connect to Gmail's IMAP server
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(EMAIL, APP_PASSWORD)
    mail.select("inbox")

    # Fetch latest emails
    status, messages = mail.search(None, "ALL")
    email_ids = messages[0].split()

    emails = []
    for e_id in email_ids[-5:]:  # Read last 5 emails
        status, msg_data = mail.fetch(e_id, "(RFC822)")
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                emails.append({
                    "From": msg['From'],
                    "Subject": msg['Subject'],
                    "Date": msg['Date']
                })

    mail.logout()
    return emails

if __name__ == "__main__":
    emails = fetch_emails()
    for email in emails:
        print(f"From: {email['From']}\nSubject: {email['Subject']}\nDate: {email['Date']}\n")