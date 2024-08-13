from django.shortcuts import render
import json
import smtplib
from email.mime.text import MIMEText
from .constants import EMAIL_SUCCESS, EMAIL_SUBJECT
import os

def send_confirmation(body):
    try:
        order_details = json.loads(body)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return

    # Construct the message
    msg = MIMEText(f"Your order with Id:{order_details['id']} is confirmed with the restraunt and will be delivered shortly!")
    msg['Subject'] = EMAIL_SUBJECT
    msg['From'] = os.getenv('USER_EMAIL')
    msg['To'] = order_details['email']

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
            smtp_server.login(os.getenv('USER_EMAIL'), os.getenv('USER_EMAIL_PASS'))
            smtp_server.sendmail(msg['From'], msg['To'], msg.as_string())
        print(EMAIL_SUCCESS)
    except smtplib.SMTPException as e:
        print(f"Error sending email: {e}")

