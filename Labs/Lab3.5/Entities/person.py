from typing import Protocol, runtime_checkable
from datetime import datetime
from re import match


# Interface analog. Full inheritance is not propriety
@runtime_checkable
class IPerson(Protocol):
    firstname: str
    lastname: str
    father_name: str
    birthday_date: str

    def person_info(self) -> str:
        ...

class Person:
    PATTERN_DATE = r"^(?:0[1-9]|[12][0-9]|3[01])-(?:0[1-9]|1[0-2])-\d{4}$"

    def __init__(self, first_name:str, last_name:str, father_name:str, birthday_date:str):
        self.first_name = first_name
        self.last_name = last_name
        self.father_name = father_name
        self.birthday_date = birthday_date #DD-MM-YYYY
        self.__check_date()
        self.age = self.calculate_age(datetime.now().strftime("%d-%m-%Y"))

    def person_info(self) -> str:
        return f"My name is {self.first_name} and last name {self.last_name}. I was born in {self.birthday_date}"

    def receive_driver_license(self) -> None:
        if self.calculate_age(self.birthday_date) < 18:
            print(f"{self.first_name} {self.last_name} is not eligible for a driver's license.")
        else:
            print(f"{self.first_name} {self.last_name} has received a driver's license.")

    def calculate_age(self, current_date: str) -> int:
        current_date_time = datetime.strptime(current_date, "%d-%m-%Y")
        birth_date = datetime.strptime(self.birthday_date, "%d-%m-%Y")

        age:int = current_date_time.year - birth_date.year

        # Adjust if birthday hasn't occurred yet this year
        if (current_date_time.month, current_date_time.day) < (birth_date.month, birth_date.day):
            age -= 1

        return age
    
    def __check_date(self) -> None:
        if match(Person.PATTERN_DATE, self.birthday_date) is None:
            raise ValueError("Invalid date format. Please use DD-MM-YYYY.")
        
    def swim(self) -> None:
        if type(self) is Person:
            print(f"{self.first_name} {self.last_name} is swimming.")
        else:
            print(f"{self.first_name} {self.last_name} is swimming (called from {type(self).__name__}).")