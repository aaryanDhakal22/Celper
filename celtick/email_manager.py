from __future__ import print_function

import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import base64

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]


def all_mails():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    # print("\n\n", os.path.exists("celtick/static/token.json"))
    # print(os.listdir())
    if os.path.exists("celtick/static/token.json"):
        creds = Credentials.from_authorized_user_file(
            "celtick/static/token.json", SCOPES
        )
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "celtick/static/credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    # Call the Gmail API
    service = build("gmail", "v1", credentials=creds)
    # request a list of all the messages
    result = service.users().messages().list(userId="me").execute()

    # We can also pass maxResults to get any number of emails. Like this:
    messages = result.get("messages")
    # print(messages)
    for msg in messages:
        # Get the message from its id
        txt = (
            service.users().messages().get(userId="me", id=msg["id"]).execute()
        )
        try:
            payload = txt["payload"]
            headers = payload["headers"]
            parts = payload.get("parts")[0]
            data = parts["body"]["data"]
            data = data.replace("-", "+").replace("_", "/")
            decoded_data = base64.b64decode(data).decode("utf-8")
            return decoded_data
        except:
            return "Error"
