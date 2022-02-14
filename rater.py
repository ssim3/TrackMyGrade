import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint

# Authorizing the API

scope = ["https://www.googleapis.com/auth/drive", "https://www.googleapis.com/auth/drive.file"]
file_name = r"C:\Users\Tristan Sim\Downloads\Kali\client_key.json"
creds = ServiceAccountCredentials.from_json_keyfile_name(file_name,scope)
client = gspread.authorize(creds)

#Fetch the sheet
sheet = client.open('LEAGUE CHAMP RATER').sheet1
python_sheet = sheet.get_all_records()
pp = pprint.PrettyPrinter()
pp.pprint(python_sheet)