import os

from Assets import Hardware, Software
from Emplyoees import Employee, Manager


def get_details_from_employee(filename:str = "employees.txt"):
    """extract employee details from employees.txt file and store in a dictionary"""
    emp_dict = {}
    if not os.path.exists(filename):
       print("Employee file not found starting from the empty data")
       return emp_dict


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
def get_details_from_assets(filename:str = "assets.txt"):
    asset_dict = {}
    if not os.path.exists(filename):
        print( "Asset file not found starting from the empty data")
        return asset_dict

    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                parts = line.split('|')
                asset_id = parts[0]
                asset_name = parts[1]
                assets_category = parts[2]
                assets_value = float(parts[3])

                if assets_category == "Hardware":
                    conditions = parts[4]
                    new_asset = Hardware(asset_id, asset_name, assets_category, assets_value, conditions)
                else:
                    expiry_date = parts[4]
                    new_asset = Software(asset_id, asset_name, assets_category, assets_value, expiry_date)

                asset_dict[asset_id] = new_asset

    print("Asset details loaded from file")
    return asset_dict


"""Load Admin Login Details Data"""
def get_details_from_admin(filename:str = "admin.txt"):
    users_dict = {}
    if not os.path.exists(filename):
        print( f"{filename} not found using the default credentials")
        #                      username , password
        users_dict["admin"] = ("admin", "admin123")
        return users_dict

    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                parts = line.split('|')
                user_role = parts[0]
                user_name = parts[1]
                user_password = parts[2]
                users_dict[user_role] = (user_name, user_password)

    print("Admin login details loaded from file")
    return users_dict


