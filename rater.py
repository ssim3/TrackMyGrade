from dataclasses import fields
from optparse import Values
from auth import spreadsheet_service
from auth import drive_service

# GREET USER AND GETS USER INPUT FOR SERVICE
def intro():
    print("""         ,----,                                                                                                                  
      ,/   .`|                                              ____                                                                
    ,`   .'  :                                 ,-.        ,'  , `.           ,----..                                            
  ;    ;     /                             ,--/ /|     ,-+-,.' _ |          /   /   \                           ,---,           
.'___,/    ,' __  ,-.                    ,--. :/ |  ,-+-. ;   , ||         |   :     :   __  ,-.              ,---.'|           
|    :     |,' ,'/ /|                    :  : ' /  ,--.'|'   |  ;|         .   |  ;. / ,' ,'/ /|              |   | :           
;    |.';  ;'  | |' | ,--.--.     ,---.  |  '  /  |   |  ,', |  ':     .--,.   ; /--`  '  | |' | ,--.--.      |   | |   ,---.   
`----'  |  ||  |   ,'/       \   /     \ '  |  :  |   | /  | |  ||   /_ ./|;   | ;  __ |  |   ,'/       \   ,--.__| |  /     \  
    '   :  ;'  :  / .--.  .-. | /    / ' |  |   \ '   | :  | :  |,, ' , ' :|   : |.' .''  :  / .--.  .-. | /   ,'   | /    /  | 
    |   |  '|  | '   \__\/: . ..    ' /  '  : |. \;   . |  ; |--'/___/ \: |.   | '_.' :|  | '   \__\/: . ..   '  /  |.    ' / | 
    '   :  |;  : |   ," .--.; |'   ; :__ |  | ' \ \   : |  | ,    .  \  ' |'   ; : \  |;  : |   ," .--.; |'   ; |:  |'   ;   /| 
    ;   |.' |  , ;  /  /  ,.  |'   | '.'|'  : |--'|   : '  |/      \  ;   :'   | '/  .'|  , ;  /  /  ,.  ||   | '/  ''   |  / | 
    '---'    ---'  ;  :   .'   \   :    :;  |,'   ;   | |`-'        \  \  ;|   :    /   ---'  ;  :   .'   \   :    :||   :    | 
                   |  ,     .-./\   \  / '--'     |   ;/             :  \  \\   \ .'          |  ,     .-./\   \  /   \   \  /  
                    `--`---'     `----'           '---'               \  ' ; `---`             `--`---'     `----'     `----'   
                                                                       `--`                                                  """)
    
    name = input("\nEnter your name: ")
    email = input("Enter your email address: ")

    print("\nSelect your service: ")
    print("1. Create blank Google Sheet")
    print("2. Record grades into existing Google Sheet (Requires sheetId from Service 1) ")

    user_choice = ""

    try:
        user_choice = int(input("\nService: "))
        if (user_choice > 3 or user_choice < 1):
            print("Enter a valid response!")
            intro()

    except ValueError:
        print("Enter a valid response!")
        intro()

    if (user_choice == 1):
        create_empty(name, email)
    elif (user_choice == 2):
        sheetId = input("Please enter the sheetId you have received from Service 1: ")
        update_records(sheetId)

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
    print("Your Sheet ID (For Service 2): " + sheetId)

    # Giving user editor permissions
    permission1 = {
        "type": "user",
        "role": "writer",
        "emailAddress": email
    }
    
    drive_service.permissions().create(fileId=sheetId, body=permission1).execute()

    value_range_body = {"majorDimension": "ROWS", "values": [["Subject", "Grade as %"]]}
    spreadsheet_service.spreadsheets().values().update(spreadsheetId=sheetId, valueInputOption = "USER_ENTERED", range = "Sheet1!A1", body=value_range_body).execute()
    
#Update records of previously created Google sheet
def update_records(sheetId):
    grades = []
    def add_grade():
        grade = [grade for grade in input("\nEnter the subject and grade as percentage separated by white space (Enter nothing if you would like to stop adding grades): ").split()]
        while (grade != []):
            grades.append(grade)
            grade = [grade for grade in input("\nEnter the subject and grade as percentage separated by white space (Enter nothing if you would like to stop adding grades): ").split()]

    add_grade()

    value_range_body = {"majorDimension": "ROWS", "values": grades}

    spreadsheet_service.spreadsheets().values().update(spreadsheetId=sheetId, valueInputOption = "USER_ENTERED", range = "Sheet1!A2", body=value_range_body).execute()
    



        


intro()






