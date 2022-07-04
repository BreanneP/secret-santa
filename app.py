import csv
import httplib2
import json
import mimetypes
import oauth2client
import os
import sys
from emails import send_message
from oauth2client import client, tools, file
from message import get_messages


client_secret_file = 'client_secret.json'
application_name = 'Gmail API Python Send Email'


def get_creds(cred_file, scope):
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    
    credential_path = os.path.join(credential_dir, cred_file)
    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(client_secret_file, scope)
        flow.user_agent = application_name
        credentials = tools.run_flow(flow, store)
        print('Storing credentials to ' + credential_path)

    return credentials


def get_names():
    names = {}
    csv_file = open('names.csv')
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        names[row[0]] = row[1]
    return names


if __name__ == '__main__':    
    names = get_names()
    results = get_messages(names)

    # get credentials
    creds = get_creds('gmail-python-email-send.json', 'https://www.googleapis.com/auth/gmail.send')
    creds = creds.authorize(httplib2.Http())

    for name, message in results.items():
        email = names.get(name)
        subject = message[0]
        msg = message[1]
        send_message(creds, email, subject, msg, msg)
