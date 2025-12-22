import os
from Emplyoees import Employee


def get_details_from_employee(filname = "employees.txt"):
    if not os.path.exists(filname):
       print("Employee file not found starting from the empty data")
       return None

    with open(filname, 'r') as file:
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

                Emp = Employee(emp_id, emp_name, emp_role, emp_salary)
                employees_list.append(Emp)
        return employees_list



a = get_details_from_employee("employees.txt")

for emp in a:
    print(emp)