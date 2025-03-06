from imapclient import IMAPClient
import email
from email.header import decode_header
import os

# Load environment variables
EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

def fetch_emails():
    """Fetch unread emails from the inbox."""
    with IMAPClient(EMAIL_HOST) as client:
        client.login(EMAIL_USER, EMAIL_PASSWORD)
        client.select_folder("INBOX")

        messages = client.search(["UNSEEN"])  # Fetch only unread emails
        fetched_emails = []

        for msg_id in messages:
            raw_msg = client.fetch([msg_id], ["RFC822"])[msg_id][b"RFC822"]
            msg = email.message_from_bytes(raw_msg)

            # Decode email subject
            subject, encoding = decode_header(msg["Subject"])[0]
            if isinstance(subject, bytes):
                subject = subject.decode(encoding or "utf-8")

            # Extract email content
            body = ""
            if msg.is_multipart():
                for part in msg.walk():
                    if part.get_content_type() == "text/plain":
                        body = part.get_payload(decode=True).decode()
                        break
            else:
                body = msg.get_payload(decode=True).decode()

            fetched_emails.append({"subject": subject, "body": body})

        return fetched_emails

import google.generativeai as genai
import os

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def extract_tasks_from_email(email_body):
    """Uses Google Gemini to extract tasks from email text."""
    genai.configure(api_key=GEMINI_API_KEY)

    prompt = f"""
    Extract key tasks from the following email:
    "{email_body}"
    Provide a clear and concise list of tasks.
    """

    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)

    return response.text.strip()
