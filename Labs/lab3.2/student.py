from typing import Protocol
from datetime import datetime

# Interface analog. Full inheritance is not propriety
class IStudent(Protocol):
    first_name: str
    last_name: str
    father_name: str
    student_id: str
    birthday_date: str
    course_number: int
    group_number: int


    def student_info(self) -> str:
        ...
    
    def transfer_to_next_course(self) -> None:
        ...
    
    def calculate_age(self, current_date: str) -> int:
        ...

class Student:
    student_amount:int = 0

    def __init__(self, first_name: str, last_name: str, father_name: str, birthday_date: str, course_number: int, group_number: int):
        self.first_name = first_name
        self.last_name = last_name
        self.father_name = father_name
        self.birthday_date = birthday_date
        self.course_number = course_number
        self.group_number = group_number
        self.student_id = f"{first_name[0]}{last_name[0]}{father_name[0]}{birthday_date.replace('-', '')}{course_number}{group_number}{Student.student_amount}"
        
        Student.student_amount += 1

    def student_info(self) -> str:
        return(
            f"My name and surname is {self.first_name} {self.last_name}, "
            f"son of {self.father_name}. I was born in {self.birthday_date}. "
            f"I study in course {self.course_number}, group {self.group_number}. My student ID is {self.student_id}."
        )

    def calculate_age(self, current_date: str) -> int:
        current_date_time = datetime.strptime(current_date, "%d-%m-%Y")
        birth_date = datetime.strptime(self.birthday_date, "%d-%m-%Y")

        age:int = current_date_time.year - birth_date.year

        # Adjust if birthday hasn't occurred yet this year
        if (current_date_time.month, current_date_time.day) < (birth_date.month, birth_date.day):
            age -= 1

        return age

    def transfer_to_next_course(self) -> None:
        if self.course_number < 5:
            self.course_number += 1
        else:
            print("You are already in the final course.")

    def __add__(self, other: "Student") -> "Student":
        if not isinstance(other, Student) and other != 0:
            raise ValueError("Can only combine with another Student")
        if other == 0:
            return self
        new_first_name = self.first_name if len(self.first_name) >= len(other.first_name) else other.first_name
        new_last_name = self.last_name if len(self.last_name) >= len(other.last_name) else other.last_name
        new_father_name = self.father_name if len(self.father_name) >= len(other.father_name) else other.father_name
        new_birthday_date = self.birthday_date if len(self.birthday_date) >= len(other.birthday_date) else other.birthday_date
        new_course_number = self.course_number + other.course_number
        new_group_number = self.group_number + other.group_number
        
        return Student(new_first_name, new_last_name, new_father_name, new_birthday_date, new_course_number, new_group_number)

    def __lt__(self, other: "Student") -> bool:
        if not isinstance(other, Student):
            raise ValueError("Can only compare with another Student")

        return self.student_id < other.student_id
