from dataclasses import fields
from auth import spreadsheet_service
from auth import drive_service

# GREET USER AND GETS USER INPUT FOR SERVICE
def intro():
    print("""     ######### ########  ##    ##     ######   ########     ###    ########  ########    ##     ## ######## 
         ##    ##     ##  ##  ##     ##    ##  ##     ##   ## ##   ##     ## ##          ###   ### ##       
         ##    ##     ##   ####      ##        ##     ##  ##   ##  ##     ## ##          #### #### ##       
         ##    ########     ##       ##   #### ########  ##     ## ##     ## ######      ## ### ## ######   
         ##    ##   ##      ##       ##    ##  ##   ##   ######### ##     ## ##          ##     ## ##       
         ##    ##    ##     ##       ##    ##  ##    ##  ##     ## ##     ## ##          ##     ## ##       
         ##    ##     ##    ##        ######   ##     ## ##     ## ########  ########    ##     ## ######## """)
    
    name = input("\nEnter your name: ")
    email = input("Enter your email address: ")

    print("\nSelect your service: ")
    print("1. Create blank Google Sheet")
    print("2. Record grades into new Google Sheet")
    print("3. Update exisitng Google Sheet")

    user_choice = ""

    try:
        user_choice = int(input("\nService: "))
        if (user_choice > 3 or user_choice < 1):
            print("Enter a valid response!")
            intro()

    except ValueError:
        print("Enter a valid response!")
        intro()

    return user_choice, name, email

# RECORD YOUR GRADES AND CREATES A SHEET FILE WITH THEM
def create_records(name, email):
    print("Hi")


# CREATES AN EMPTY SHEETS FILE
def create_empty(name, email):

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
        "emailAddress": email
    }
    
    drive_service.permissions().create(fileId=sheetId, body=permission1).execute()
    return sheetId

def update_records(name, email):
    print("hi")


choice, name, email = intro()


