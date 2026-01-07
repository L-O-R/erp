#========================================
# phase 3
#========================================
from employee_sub_menu import employee_sub_menu
from input_validation import get_user_choice


def display_main_menu(user:dict):
    """
    Display the main menu
    this is a central hub
    After every action returns the user here
    :return: None
    """
    print()
    print("=" * 50)
    print(f"Main Menu - Welcome {user["username"]}")
    print("=" * 50)
    print()
    print("Select an option(in number format 1-4):")
    print("1. Manage Employees")
    print("2. Manage Assets")
    print("3. Company Financials")
    print("4. Save & Exit")
    print("=" * 50)


def main_menu_loop(users:dict, employees:dict, assets:dict ):
    """
    Phase 3
    this is an infinite loop until user select an option = Save & Exit
    Flow:
    1. Display the main menu
    2. Get the user Choice
    3. Execute action
    4. Return to step 1
    5. Only save and exit will end the loop
    :param users: dictionary of logined user(username and role)
    :param employees: dictionary of employee details(id, name, role, salary, bonus)
    :param assets: dictionary of assets details(id, name, category, value, conditions, expiry date)
    :return: boolean
    """

    running = True
    while running:
        #1. Display the main menu
        display_main_menu(users)

        # 2. Get the user choice
        choice = get_user_choice()

        match choice:
            case 1:
                print("Loading Employees Sub Menu....")
                employee_sub_menu(employees)
            case 2:
                print("Loading Assets Sub Menu....")
            case 3:
                print("Loading Company Financials Sub Menu....")
            case 4:
                print("=" * 50)
                print("Saving & Exiting")
                print("=" * 50)
                confirm = input("Do you want to save & exit (y/n): ")
                if confirm == "y":
                    print()
                    print("Saving the Data....")
                    print("System Shutting Down...")
                    running = False
                else:
                    print()
                    print("Cancelled! Returning to the main menu...")

    return True # signals the user wants to exit

