from turtle import title
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint
from googleapiclient import discovery

# Authorizing the API

scope = ["https://www.googleapis.com/auth/drive", "https://www.googleapis.com/auth/drive.file"]
file_name = r"C:\Users\Tristan Sim\Downloads\Kali\client_key.json"
creds = ServiceAccountCredentials.from_json_keyfile_name(file_name,scope)
client = gspread.authorize(creds)

service = discovery.build("sheets", "v4", credentials=creds)

spreadsheet = {"properties": {"title": title}}

spreadsheet = service.spreadsheets().create(body = spreadsheet, fields = "Grade Tracker").execute()
print(spreadsheet.get("Grade Tracker"))

    