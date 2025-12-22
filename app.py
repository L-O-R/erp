from difflib import Match

import Menu
"""
    login Logic
"""
login = False
tries = 1
with open('loginCredientials.txt', 'r') as credFile:
    creds = credFile.readlines()
    while tries < 4:
        user_name = input('Enter your username: ')
        if creds[0].strip() == user_name:
            password = input('Enter your password: ')
            if password == creds[1].strip():
                login = True
                break
            else:
                print(f'Wrong password , Tries left {3- tries}')
                tries += 1
        else:
            print(f'Wrong username , Tries left {3- tries} ')
            tries += 1


    credFile.close()
#------------------------------------

"""
    display the menu 
"""
userChoice = None
while login and userChoice != 4 :
    Menu.display_menu()
    userChoice = int(input('Enter your choice (Ex. 1): '))
    match userChoice:
        case 4:
            print("Exiting and saving the changes")
            print("Thankyou for using erp management")
            break
        case _:
            print(f'Wrong choice , please enter in a number format only from 1 to 4')