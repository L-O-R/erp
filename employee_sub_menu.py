from Emplyoees import Manager, Employee
from input_validation import get_user_choice, validate_name, validate_role, validate_number


def display_sub_menu():
    print()
    print("=" * 50)
    print("             Employee Sub Menu")
    print("=" * 50)
    print()
    print("1. Add Employee")
    print("2. View All Employee")
    print("3. Update Employee")
    print("4. Delete Employee")
    print("5. Back to main menu")
    print()
    print("=" * 50)

def generate_id(employee_dict:dict):
    if not employee_dict:
        return "E001"

    existing_emp_id_list = []
    for employee_id in employee_dict.keys():
        emp_id = employee_id.replace("E", "") # 001, 002
        existing_emp_id_list.append(emp_id)
#004 +1 005
    next_id = max(existing_emp_id_list) + 1
    return f"E{next_id}" # E003





# add employee
def add_employee(employee_dict:dict):
    emp_id = generate_id(employee_dict)
    name = validate_name()
    role = validate_role()
    salary = validate_number("Enter employee salary: ")
    if role.lower() == "manager":
        bonus = validate_number("Enter bonus: ")
        employee = Manager(emp_id, name, role, salary, bonus)
    else:
        employee = Employee(emp_id,name, role, salary)

    print(f"Employee Was created successfully: {employee.id}")
    print(employee.get_details())
    employee_dict[emp_id] = employee
    return employee_dict
# {
#     "E001": {
#         "name": "",
#         "role": "",
#         "salary": 0
#     }
# }

def view_employee():
    pass

def update_employee():
    pass

def delete_employee():
    pass

def employee_sub_menu(employee_dict:dict):
    while True:
        #display the sub menu
        display_sub_menu()

        user_input = get_user_choice(("1","2","3","4","5"))

        match user_input:
            case 1:
                 add_employee(employee_dict)
            case 2:
                view_employee()
            case 3:
                update_employee()
            case 4:
                delete_employee()

            case 5:
                print("going back to main menu....")
                print()
                return  employee_dict

