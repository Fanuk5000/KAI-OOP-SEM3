from typing import Protocol
from datetime import datetime
from re import match

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
    PATTERN_DATE = r"^(?:0[1-9]|[12][0-9]|3[01])-(?:0[1-9]|1[0-2])-\d{4}$"\
    
    def __init__(self, first_name: str, last_name: str, father_name: str, birthday_date: str, course_number: int, group_number: int, student_id: str = ""):
        self.first_name = first_name
        self.last_name = last_name
        self.father_name = father_name
        self.birthday_date = birthday_date

        self.__check_date()
        self.course_number = course_number
        self.group_number = group_number
        self.student_id = f"{first_name[0]}{last_name[0]}{father_name[0]}{birthday_date.replace('-', '')}{course_number}{group_number}"

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

    def __check_date(self) -> None:
        if match(Student.PATTERN_DATE, self.birthday_date) is None:
            raise ValueError("Invalid date format. Please use DD-MM-YYYY.")
    
    def transfer_to_next_course(self) -> None:
        if self.course_number < 5:
            self.course_number += 1
        else:
            print("You are already in the final course.")

    def __lt__(self, other: "Student") -> bool:
        if not isinstance(other, Student):
            raise ValueError("Can only compare with another Student")

        return self.student_id < other.student_id

    def __gt__(self, other: "Student") -> bool:
        if not isinstance(other, Student):
            raise ValueError("Can only compare with another Student")

        return self.student_id > other.student_id
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Student):
            raise ValueError("Can only compare with another Student")
        return self.student_id == other.student_id