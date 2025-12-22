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