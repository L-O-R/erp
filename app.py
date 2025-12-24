# phase 1.4
from read_write import get_details_from_employee


def startup_phase():
    print("=" * 50)
    print("NexGen Solutions ERP")
    print("=" * 50)

    print("Loading data from the file")
    employees = get_details_from_employee("employees.txt")

    """asset """
    assets = {}

    print()
    print("=" * 50)
    print("Booting up the menu! Please Wait......")
    print("=" * 50)
    return employees, assets

