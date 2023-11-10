from Assets.Codes import return_config
from Assets.Codes import bcolors as ccolors
from Assets.Codes import getPointCell
from Assets.Codes import ConnectGoogle
import pandas as pd
from os import system, name, path

def clearConsole():
    system('cls' if name == 'nt' else 'clear')

googleConnect = ConnectGoogle(path.dirname(__file__)) #It retrieves the Credentials token from the config file 
                                                      #and creates a new one if the config file doesn't exist 
                                                      # or replaces it if it's corrupted.

config = return_config(path.dirname(__file__)+r"\Assets\Config\sheet_config.ini")
SHEET_NAME = config["Sheet"]["SheetName"]

sheet = googleConnect.open(SHEET_NAME)[0]

userList = []
while True:
    print("""
             To create officer list for add shift score: 1
             To add shift score to officers: 2 (The list will be deleted)
             To show officer list: 3
          """)
    choice = str(input("Your choice: "))

    if choice == "1":
        clearConsole()
        print("""
                 Enter 'e' for back to main menu.
                 Enter 'l' for add multiple officer (Names must be separated by commas.)
              """)
        while True:
            getInput = str(input("Enter Officer Name: "))
            if getInput.lower() == "e":
                clearConsole()
                break

            elif getInput.lower() == "l":
                getListInput = str(input("\nEnter Officer List: "))
                try:
                    rowRange = (int(config["SheetRangeRow"]["From"]), int(config["SheetRangeRow"]["To"]))
                    colRange = (int(config["SheetRangeCol"]["From"]), int(config["SheetRangeCol"]["To"]))
                    for staffName in getListInput.split(", "): 
                        staffL = sheet.find(staffName, rows=rowRange, cols=colRange)
                        if staffL in userList:
                            print(ccolors.WARNING + f"!! The entered person {ccolors.OKGREEN}{staffName}{ccolors.WARNING} is already in the list. Please check the list." + ccolors.OKCYAN + f" ({staffL[0].value})" + ccolors.ENDC)
                        elif staffL != []:
                            if staffL[0].label[0] == "B" or staffL[0].label[0] == "G":
                                userList.append(staffL)
                            else:
                                print(ccolors.WARNING + "!! The entered person was not found. Make sure that the name exists in Sheet or was entered correct." + ccolors.OKCYAN + f" ({staffName})" + ccolors.ENDC)
                        else:
                            print(ccolors.WARNING + "!! The entered person was not found. Make sure that the name exists in Sheet or was entered correct." + ccolors.OKCYAN + f" ({staffName})" + ccolors.ENDC)
                except:
                    print(ccolors.FAIL + "!!! Error occured while querying. Please try again." + ccolors.ENDC)
            else:           
                try:
                    rowRange = (int(config["SheetRangeRow"]["From"]), int(config["SheetRangeRow"]["To"]))
                    colRange = (int(config["SheetRangeCol"]["From"]), int(config["SheetRangeCol"]["To"]))
                    staff = sheet.find(getInput, rows=rowRange, cols=colRange)
                    if staff in userList:
                        print(ccolors.WARNING + "!! The entered person is already in the list. Please check the list." + ccolors.ENDC)
                    elif staff != []:
                        if staff[0].label[0] == "B" or staff[0].label[0] == "G":
                            userList.append(staff)
                        else:
                            print(ccolors.WARNING + "!! The entered person was not found. Make sure that the name exists in Sheet or was entered correct." + ccolors.ENDC)
                    else:
                        print(ccolors.WARNING + "!! The entered person was not found. Make sure that the name exists in Sheet or was entered correct." + ccolors.ENDC)
                except:
                    print(ccolors.FAIL + "!!! Error occured while querying. Please try again." + ccolors.ENDC)

    
    elif choice == "2":
        clearConsole()
        if userList:
            data2 = []
            for i in userList:

                oldPoint = sheet.get_value(getPointCell(i))
                newPoint = int(oldPoint)+1

                LOPEZ_GROUP = config["PointCellGroup"]["LOPEZ"]

                team = "LOPEZ" if i[0].label[0] == LOPEZ_GROUP else "GOMEZ"
                data2.append([i[0].value, oldPoint, newPoint, team])
                sheet.update_value(getPointCell(i), newPoint)

            df = pd.DataFrame(data2, columns=["Name Surname", "Score", "New Score", "Team"])
            clearConsole()
            print(df)
            print("""----------------------------------------------------------------------------------------
                """)
            print("""
                        The attendance score of the officers in the above list has been increased by 1.""")
            userList.clear()
            df = None
            data2 = None
        else:
            clearConsole()
            print(f"""{ccolors.FAIL}The employees list is empty! Choice the first option from the list then enter the person that you want to assing shift point to.{ccolors.ENDC}
----------------------------------------------------------------------------------------""")

    elif choice == "3":
        if userList:
            data = []
            for i in userList:
                point = sheet.get_value(getPointCell(i))

                LOPEZ_GROUP = config["PointCellGroup"]["LOPEZ"]

                team = "LOPEZ" if i[0].label[0] == LOPEZ_GROUP else "GOMEZ"
                data.append([i[0].value, point, team])

            df = pd.DataFrame(data, columns=["Name Surname", "Score", "Team"])
            clearConsole()
            print(df)
            print("""----------------------------------------------------------------------------------------
                  """)
            df = None
            data = None
        else:
            clearConsole()
            print(f"""{ccolors.FAIL}The employees list is empty! Choice the first option from the list then enter the person that you want to assing shift point to.{ccolors.ENDC}
----------------------------------------------------------------------------------------""")
    else:
        clearConsole()
