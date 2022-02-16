from dataclasses import fields
from auth import spreadsheet_service
from auth import drive_service

# FUNCTIONS
def intro():
    print("""     ######### ########  ##    ##     ######   ########     ###    ########  ########    ##     ## ######## 
         ##    ##     ##  ##  ##     ##    ##  ##     ##   ## ##   ##     ## ##          ###   ### ##       
         ##    ##     ##   ####      ##        ##     ##  ##   ##  ##     ## ##          #### #### ##       
         ##    ########     ##       ##   #### ########  ##     ## ##     ## ######      ## ### ## ######   
         ##    ##   ##      ##       ##    ##  ##   ##   ######### ##     ## ##          ##     ## ##       
         ##    ##    ##     ##       ##    ##  ##    ##  ##     ## ##     ## ##          ##     ## ##       
         ##    ##     ##    ##        ######   ##     ## ##     ## ########  ########    ##     ## ######## """)

    print("\nSelect your service: ")
    print("1. Create blank Google Sheet")
    print("2. Record grades into new Google Sheet")
    print("3. Update exisitng Google Sheet")
    
def create(name, email):
    spreadsheet_details = {
        "properties": {
            "title": "TrackMyGrade - {}".format(name)
        }
    }

    # CREATES AN GOOGLE SHEET 
    sheet = spreadsheet_service.spreadsheets().create(body=spreadsheet_details, fields="spreadsheetId").execute()

    # GETS GOOGLE SHEET ID
    sheetId = sheet.get("spreadsheetId")
    print("Your spreadsheet link: https://docs.google.com/spreadsheets/d/{0}/edit#gid=0".format(sheetId))

    permission1 = {
        "type": "user",
        "role": "writer",
        "emailAddress": "tristansimtristansim@gmail.com"
    }
    
    drive_service.permissions().create(fileId=sheetId, body=permission1).execute()
    return sheetId



intro()