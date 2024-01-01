import base64, os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from email.message import EmailMessage
from PlayfairCipher import MessageReady
import os
import time
import re

#EMAIL_ADDRESS = os.environ.get('EMAIL_USER')

def user_authorization():
    SCOPES = ["https://www.googleapis.com/auth/gmail.send"]
    creds = None
 
    print("Before you send anything, you must be authorized...")
    try:
        if os.path.exists("token.json"):
            print("Checking for Token...")
            creds = Credentials.from_authorized_user_file("token.json", SCOPES)
            print("Access granted!")
    except:
            print("Access denied!")
            time.sleep(2)
            raise Exception()
                
  # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            try:
                print("Refreshing credentials...")
                creds.refresh(Request())
            except:
                print("Credentials are unavailable! Exiting...")
                time.sleep(2)
                raise Exception()
        else:
            try:
                print("Creating new Token...")
                flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
                creds = flow.run_local_server(port=0)
            except:
                print("Unable to create token! Authorization is impossible. Exiting...")
                time.sleep(2)
                raise Exception()
                                 # Save the credentials for the next run
        try:
            with open("token.json", "w") as token:
                token.write(creds.to_json())
                print("New Token saved!")
        except:
            print("token.json could not be saved! Exiting...")
            time.sleep(2)
            raise Exception()
            
    return creds
    


def mail_writeit():
      receiver = MailValidation()
      subject = input("Subject: ")
      body = MessageReady()
      return receiver, subject, body
      
      
     
      

def mail_build(): 

    creds = user_authorization()

    receiver, subject, body=mail_writeit()
    
    
    service = build("gmail", "v1", credentials=creds)
    message = EmailMessage()
    message['Subject'] = subject
    #message['From'] = EMAIL_ADDRESS
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
        return 0
        
        

  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.

def checkNsend(message, service):
    
    
    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode("utf-8")

    message = service.users().messages().send(userId="me", body={'raw': raw_message}).execute()

def MailValidation():
    email_pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    print("Checking E-maiil address validity...")    
    
    address = input("Receiver: ")

    while not re.match(email_pattern, address):
        print("E-Mail address is not valid! Try again...")
        address = input("Receiver: ")
    
    print("E-Mail address is valid.")
    return address

    #return bool(re.match(email_pattern, address))

    

