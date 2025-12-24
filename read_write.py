import os
from Emplyoees import Employee, Manager


def get_details_from_employee(filename:str = "employees.txt"):
    """extract employee details from employees.txt file and store in a dictionary"""
    emp_dict = {}
    if not os.path.exists(filename):
       return "Employee file not found starting from the empty data"


    with open(filename, 'r') as file:
        #will go through each line
        # readlines
        employees_list = []
        for line in file:
            line = line.strip()
            if line:
                parts = line.split('|')
                emp_id = parts[0]
                emp_name = parts[1]
                emp_role = parts[2]
                emp_salary = float(parts[3])
                if emp_role == "Manager":
                    bonus = float(parts[5])
                    employee = Manager(emp_id, emp_name, emp_role, emp_salary, bonus)
                else:
                    employee = Employee(emp_id, emp_name, emp_role, emp_salary)

                emp_dict[emp_id] = employee
    print("Employee details loaded from file")
    return emp_dict


"""Load assets data from assets.txt file"""


