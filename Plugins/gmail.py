import os
import smtplib
import re
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENV_PATH = os.path.join(BASE_DIR, 'Data', '.env')
load_dotenv(dotenv_path=ENV_PATH)

sender_id = os.getenv("EMAIL_ID")
password = os.getenv("PASSWORD")

def send_email(receiver_id, subject, body):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(sender_id, password)

    message = "\r\n".join([
        f"From: {sender_id}",
        f"To: {receiver_id}",
        f"Subject: {subject}",
        "",
        f"{body}"
    ])

    try:
        s.sendmail(sender_id, receiver_id, message)
    except smtplib.SMTPRecipientsRefused:
        print("Invalid Email Address")
        return False
    except smtplib.SMTPException:
        return False
    finally:
        s.quit()

    return True

def check_email(email_id):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.fullmatch(pattern, email_id) is not None
