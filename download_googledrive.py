import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pandas as pd

SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# Reference: https://developers.google.com/sheets/api/quickstart/python
def read_google_sheets(SPREADSHEET_ID, RANGE_NAME, HEADER_RANGE):
    creds = None
    # autogenerated
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                range=RANGE_NAME).execute()
    
    header = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                               range=HEADER_RANGE).execute()
    
    header_values = header.get('values', [])
    values = result.get('values', [])
    
    return values, header_values

def main():
    # variable_metadata = pd.read_csv("etc/variables.csv")

    # Data sheet
    print("Downloading data into data.csv")
    SPREADSHEET_ID = '15v6tmhVXha1wUiy-6j1ZsNEgj-Dai73U7PJ8NWKuwJk'
    RANGE_NAME = "'Parlametrics Codings'!A2:BQ189"
    HEADER_RANGE = "'Parlametrics Codings'!A1:BQ1"
    data, header = read_google_sheets(SPREADSHEET_ID, RANGE_NAME, HEADER_RANGE)
    data_df = pd.DataFrame(data, columns = header[0])
    # keep_columns = variable_metadata.loc[(variable_metadata["table"] == "data") & (variable_metadata["visibility"] == "public")]
    # data_df = data_df.filter(items = keep_columns["name"])
    data_df.to_csv('raw/data.csv', index=False)
    print("successful")

    # Song metadata sheet
    print("Downloading conversation metadata into conversation.csv")
    SPREADSHEET_ID = '1Ojbj-2SfbxTYM_Da-uxdpoR9aZEqwfVt9dWouFeRa80'
    RANGE_NAME = "'Metadata (in progress)'!A3:BA225"
    HEADER_RANGE = "'Metadata (in progress)'!A2:BA2"
    data, header = read_google_sheets(SPREADSHEET_ID, RANGE_NAME, HEADER_RANGE)
    songs_df = pd.DataFrame(data, columns = header[0])
    # keep_columns = variable_metadata.loc[(variable_metadata["table"] == "songs") & (variable_metadata["visibility"] == "public")]
    # songs_df = songs_df.filter(items = keep_columns["name"])
    songs_df.to_csv('raw/conversation.csv', index=False)
    print("successful")

    # Society metadata sheet
    print("Downloading society metadata into societies.csv")
    SPREADSHEET_ID = '1tb3Nip43e4LaJbglaXzcCTP2CiMyrgwIsU2egk3tfNM'
    RANGE_NAME = "'All Cultures'!A2:BA1247"
    HEADER_RANGE = "'All Cultures'!A1:BA1"
    data, header = read_google_sheets(SPREADSHEET_ID, RANGE_NAME, HEADER_RANGE)
    society_df = pd.DataFrame(data, columns = header[0])
    # keep_columns = variable_metadata.loc[(variable_metadata["table"] == "societies") & (variable_metadata["visibility"] == "public")]
    # society_df = society_df.filter(items = keep_columns["name"])
    society_df = society_df[society_df.P_cid != ""]
    society_df.to_csv('raw/societies.csv', index=False)
    print("successful")

main()
