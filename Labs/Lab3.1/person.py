class Person:
    def __init__(self, firstname:str, lastname:str, birthday_date:str):
        self.firstname = firstname
        self.lastname = lastname
        self.birthday_date = birthday_date #DD-MM-YYYY

    def person_info(self):
        return f"My name is {self.firstname} and last name {self.lastname}. I was born in {self.birthday_date}"