from typing import Protocol, runtime_checkable

# Interface analog. Full inheritance is not propriety
@runtime_checkable
class IPerson(Protocol):
    firstname: str
    lastname: str
    birthday_date: str

    def person_info(self) -> str:
        ...

class Person:
    def __init__(self, firstname:str, lastname:str, birthday_date:str):
        self.firstname = firstname
        self.lastname = lastname
        self.birthday_date = birthday_date #DD-MM-YYYY

    def person_info(self):
        return f"My name is {self.firstname} and last name {self.lastname}. I was born in {self.birthday_date}"


# To check: python person.py
if __name__ == "__main__":
    # To test if Person uses interface of IPerson
    person = Person("John", "Doe", "12-12-1212")
    print(isinstance(person, IPerson))