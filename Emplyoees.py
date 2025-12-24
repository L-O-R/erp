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
        self.name = name

    @property
    def role(self):
        return self.__role
    @role.setter
    def role(self, role:str):
        self.role = role

    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self, salary:float):
        self.salary = salary

    @property
    def assets(self):
        return self.__assets

    def assign_assets(self, assets_assigned):
        return self.assets.append(assets_assigned)

    def get_details(self):
        assets = ", ".join(self.assets)
        return f"Id: {self.id} | Name: {self.name} | Role: {self.role} | Salary: {self.salary} | Assigned Assets: {assets} "

    def __str__(self):
        return self.get_details()
    def __repr__(self):
        return self.get_details()



class Manager(Employee):
    def __init__(self, emp_id:str, name:str, role:str, salary:float, bonus:float = 1000):
         super().__init__(emp_id, name, role, salary)
         self.__bonus = bonus

    @property
    def get_bonus(self):
        return self.__bonus

    @property
    def total_calculation(self):
        return self.get_bonus + self.salary

    #method overriding
    def get_details(self):
        base_details = super().get_details()
        return base_details + f"| bonus: {self.get_bonus}"