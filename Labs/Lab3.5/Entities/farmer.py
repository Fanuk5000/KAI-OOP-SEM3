from person import Person

class Farmer(Person):
    def __init__(self, first_name: str, last_name: str, father_name: str, birthday_date: str, farm_name: str):
        super().__init__(first_name, last_name, father_name, birthday_date)
        self.farm_name = farm_name

    def farmer_info(self) -> str:
        return (
            f"My name is {self.first_name} {self.last_name}, son of {self.father_name}. "
            f"I was born on {self.birthday_date} and I own the farm named {self.farm_name}."
        )