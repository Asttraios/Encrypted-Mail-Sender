import smtplib, ssl, getpass, base64, os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from email.message import EmailMessage

pass_error = "Wrong password, try again!"
EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
#EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')




def user_authorization():
    SCOPES = ["https://www.googleapis.com/auth/gmail.send"]
    creds = None

    if os.path.exists("token.json"):
        print("Before you send anything, you must be authorized! Checking for token...")
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
        print("Token is valid!")
  # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            print("Refreshing token...")
            creds.refresh(Request())
        else:
            print("Token not found. Creating new...")
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
        )
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())
            print("Token saved!")
    return creds
    


def mail_writeit():
      receiver = input("Receiver: ")
      subject = input("Subject: ")
      body = input("Write down the message: ")
      return receiver, subject, body
      

def mail_build(): 

    receiver, subject, body=mail_writeit()
    creds = user_authorization()
    
    service = build("gmail", "v1", credentials=creds)
    message = EmailMessage()
    message['Subject'] = subject
    message['From'] = EMAIL_ADDRESS
    message['TO'] = receiver
    message.set_content(body)
    
    checkNsend(message, service)
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.

#password = input("Enter your passwod: ")
# Send email here
def checkNsend(message, service):
    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode("utf-8")

    message = service.users().messages().send(userId="me", body={'raw': raw_message}).execute()

