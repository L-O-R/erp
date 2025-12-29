# ============================================
# NEXGEN CORPORATE ECOSYSTEM (NCE)
# PHASE 1: THE STARTUP (The Loading Phase)
# PHASE 2: THE LOGIN GATE (Access Control)
# ============================================


"""
PHASE 1:
-------------------
Before the user sees ANYTHING on screen, the program needs to "wake up."

What happens here:
1. Check if data files exist (employees.txt, assets.txt)
2. If files exist → Read them and convert text back into Python Objects
3. If files don't exist → Start with empty dictionaries
4. Prepare the system for user interaction

Think of this like a computer booting up - it needs to load everything
into memory (RAM) before you can use it.
"""
from Menu import main_menu_loop

"""
PHASE 2:
-------------------
After the system boots up, the user sees a LOGIN SCREEN.

What happens here:
1. User is prompted for Username and Password
2. System verifies credentials against stored data
3. User has MAXIMUM 3 attempts
4. After 3 failed attempts → System locks and closes
5. On success → Move to Main Menu (Phase 3)

This is SECURITY - prevents unauthorized access to the system.
"""

"""
PHASE 3:
-------------------
After succesfull Login, users sees the main menu.

What happens here:
1. Display 4 menus => manage emplyoees, assets, company financials, save and exit
2. User Selects and option (1-4)
3. System excutes the selected options
4. After Action completes => Return TO main menu
5. ONly "Save and Exits" breaks the loop 

This is the central Hub => all navigation starts here
"""


# phase 1.4
from read_write import get_details_from_employee, get_details_from_assets, get_details_from_admin


def startup_phase():
    print("=" * 50)
    print("NexGen Solutions ERP")
    print("=" * 50)

    print("Loading data from the file")
    employees = get_details_from_employee("employees.txt")

    """asset """
    assets = get_details_from_assets("assets.txt")

    print()
    print("=" * 50)
    print("Booting up the menu! Please Wait......")
    print("=" * 50)
    return employees, assets


def login_phase():
    """
    phase 2
    What happens here:
    1. Load user credientials from file
    2. Prompt user for username and password
    3. Verify credentials against stored data
    4. User has MAXIMUM 3 attempts
    :return: user details on success or none
    """

    print("=" * 50)
    print("              Login Required")
    print("=" * 50)
    print()

    #load user credientials
    users = get_details_from_admin('admin.txt')
    print('staff' in users)
    #track attempts
    max_attempts = 3
    attempts = 1

    while attempts <= max_attempts:
        print("=" * 50)
        print(f"Attempts {attempts} of {max_attempts}")
        print("=" * 50)
        # whenever you are using input u will get the output in str data type
        #get role
        role = input("Please enter your role: ")

        #verify the credientials
        if role in users:
            stored_username, stored_password = users[role]
            # get username
            username = input("Username: ")
            if username == stored_username:
                # get password
                password = input("Password: ")
                if password == stored_password:

                    #Success
                    print()
                    print("Login Successful! ")
                    print(f"Welcome {username}! (Role: {role})")
                    print("=" * 50)
                    print()
                    return {"username": username, "role": role}
                else:
                    print("Invalid Credentials, Password wrong!")
                    attempts += 1
                    continue
            else:
                print(f"Username {username} not matched.")
                attempts += 1
                continue
        else:
            print('Invalid Role , Please try again.')
            attempts += 1
            continue

    print("=" * 50)
    print("Security Breach")
    print("=" * 50)
    print("Maximum Attempts reached")
    print("=" * 50)

    print()
    return None



if __name__ == "__main__":
    employees, assets = startup_phase()

    users = login_phase()
    if users is None:
        print("System clossing ...")
    else:
        exit_requested = main_menu_loop(users,employees, assets)
        if exit_requested:
            print("=" * 50)
            print("Thank you for using  NEXGEN CORPORATE ECOSYSTEM (NCE)")


