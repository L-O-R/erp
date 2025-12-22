class Employee:
    def __init__(self, emp_id:str, name:str, role: str, salary:float):
        self.__id = emp_id
        self.__name = name
        self.__role = role
        self.__salary = salary
        self.__assets = []

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name:str):
        self.__name = name

    @property
    def role(self):
        return self.__role
    @role.setter
    def role(self, role:str):
        self.__role = role

    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self, salary:float):
        self.__salary = salary

    @property
    def assets(self):
        return self.__assets

    def get_details(self):
        # for assets
        # assets_str = ",".join([])
        return f"Id: {self.id} | Name: {self.name} | Role: {self.role} | Salary: {self.salary} "
    #print(obj)
    def __str__(self):
        return self.get_details()

