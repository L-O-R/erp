def get_user_choice(li:tuple = ("1","2","3",'4')):
    """
    Get the user choice and validate it

    :return: user choice
    """
    while True:
        try:
            choice = input("Please select an option: ")
            if choice in li:
                return int(choice)
            else:
                print("Invalid choice. Please try again (1-4).")
        except ValueError:
            print("Invalid choice. Please Enter a Number (1-4).")


def validate_name():
    while True:
        user_name = input("Please enter Employee name: ").strip()
        if user_name == "":
            print("Invalid name. Please try again.")
            continue
        else:
            return user_name

def validate_role():
    while True:
        role = input("Please enter Employee role: ").strip()
        if role == "":
            print("Invalid role. Please try again.")
            continue
        elif role not in ["manager", "staff", "Manager", "Staff"]:
            print("Invalid role. Please try again. Please add oly Manager and Staff")
            continue
        else:
            return role

def validate_number(text):
    while True:
        number = input(text).strip()
        if number == "":
            print("Invalid number. Please try again.")
            continue
        elif number.isdigit():
            return float(number)
        else:
            print("Invalid number. Please try again.")
            continue
