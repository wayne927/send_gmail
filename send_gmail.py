from __future__ import print_function
import pickle
from googleapiclient.discovery import build
from email.mime.text import MIMEText
import base64
import os

def create_message(to_address, subject, text) :
    message = MIMEText(text, _charset='utf-8');
    message['to'] = to_address
    message['from'] = 'me'
    message['subject'] = subject
    return { 'raw': base64.urlsafe_b64encode(message.as_string().encode()).decode() }
    # The extra .encode() and .decode() is to get around a python3 issue.
    # On python2 the following is sufficient
    # return { 'raw': base64.urlsafe_b64encode(message.as_string()) }

def send_message(service, message) :
    result = ( service.users().messages().send(userId='me', body=message).execute() )
    return result

def send_gmail(to_address, subject_text, body_text) :
    creds = None
    if os.path.exists('token.pickle') :
        with open('token.pickle', 'rb') as token :
            creds = pickle.load(token)
    else :
        print('No credentials')
        exit()

    service = build('gmail', 'v1', credentials=creds)

    msg = create_message(to_address, subject_text, body_text)
    result = send_message(service, msg)
    print('Email sent. Message ID: ' + result['id'])

