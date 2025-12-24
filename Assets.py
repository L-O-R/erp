class Assets:
    def __init__(self,asset_id:str, name: str, value: float, category:str):
        self.__asset_id = asset_id
        self.__name = name
        self.__value = value
        self.__category = category

    @property
    def asset_id(self):
        return self.__asset_id

    @property
    def name(self):
        return self.__name

    @property
    def value(self):
        return self.__value

    @property
    def category(self):
        return self.__category

    def get_details(self):
        return f"ID: {self.asset_id} | Name:  {self.name} | Value: {self.value} | Asset type: {self.category}"

    def __str__(self):
        return self.get_details()

class Hardware(Assets):
    def __init__(self,asset_id:str, name: str, value: float, category:str, condition:str):
        super().__init__(asset_id, name, value, category)
        self.__condition = condition

    @property
    def get_condition(self):
        return self.__condition

    @get_condition.setter
    def get_condition(self, condition:str):
        self.get_condition = condition


    def get_details(self):
        base_details = super().get_details()
        return base_details + f"| condition: {self.get_condition}"

class Software(Assets):
    def __init__(self, asset_id: str, name: str, value: float, category: str, expiry_date: str):
        super().__init__(asset_id, name, value, category)
        self.__expiry_date = expiry_date

    @property
    def get_expiry_date(self):
        return self.__expiry_date

    @get_expiry_date.setter
    def get_expiry_date(self, expiry_date: str):
        self.get_expiry_date = expiry_date

    def get_details(self):
        base_details = super().get_details()
        return base_details + f"| expiry_date: {self.get_expiry_date}"
