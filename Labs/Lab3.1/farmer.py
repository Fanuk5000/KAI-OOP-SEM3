from person import Person

class Farmer(Person):
    def __init__(self, firstname:str, lastname:str, birthday_date:str, farm_location:str) -> None:
        super().__init__(firstname, lastname, birthday_date)
        self.farm_location = farm_location

    def farmer_info(self):
        return f"{super().person_info()} My farm is located at {self.farm_location}."