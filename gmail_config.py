import base64, os
from math import e
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from email.message import EmailMessage
from PlayfairCipher import MessageReady
import os
import time

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
#EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')



def user_authorization():
    SCOPES = ["https://www.googleapis.com/auth/gmail.send"]
    creds = None

    try:
        if os.path.exists("token.json"):
            print("Before you send anything, you must be authorized! Checking for token...")
            creds = Credentials.from_authorized_user_file("token.json", SCOPES)
            print("Token is valid!")
    except FileNotFoundError as e:
        print(e)
        time.sleep(2)
        raise FileNotFoundError("No such file or directory: 'credentials.json' ")    

  # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            try:
                print("Refreshing credentials...")
                creds.refresh(Request())
            except:
                print("Credentials are unavailable!")
        else:
            try:
                print("Token not found. Creating new...")
                flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
                creds = flow.run_local_server(port=0)
            except FileNotFoundError:
                print("Unable to create token - credentials.json not found! Authorization is impossible. Exiting...")
                time.sleep(2)
                raise FileNotFoundError("Error. Unable to check if Token is valid! Exiting...")
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())
            print("Token saved!")
    return creds
    


def mail_writeit():
      receiver = input("Receiver: ")
      subject = input("Subject: ")
      body = MessageReady()
      return receiver, subject, body
      

def mail_build(): 

    creds = user_authorization()

    receiver, subject, body=mail_writeit()
   
    
    service = build("gmail", "v1", credentials=creds)
    message = EmailMessage()
    message['Subject'] = subject
    message['From'] = EMAIL_ADDRESS
    message['TO'] = receiver
    message.set_content(body)
    
    
    user_confirm = input("Confirm? Y/N: ").strip().lower()
    
    if(user_confirm=='y'):
        os.system('cls')      
        print("Building...\n")
        checkNsend(message, service)
        print("E-Mail has been sent!\n Press any key to go back to menu...")
        input()
        
    else:
        os.system('cls')
        print("Discarding message...")
        time.sleep(2)
        

  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.

def checkNsend(message, service):
    
    
    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode("utf-8")

    message = service.users().messages().send(userId="me", body={'raw': raw_message}).execute()

