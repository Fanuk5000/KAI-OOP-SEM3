from typing import Protocol
from Entities.person import Person

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

class Student(Person):
    def __init__(self, first_name: str, last_name: str, father_name: str, birthday_date: str, course_number: int, group_number: int, student_id: str = ""):
        super().__init__(first_name, last_name, father_name, birthday_date)

        self.course_number = course_number
        self.group_number = group_number
        self.student_id = f"{first_name[0]}{last_name[0]}{father_name[0]}{birthday_date.replace('-', '')}{course_number}{group_number}"

    def student_info(self) -> str:
        return(
            f"My name and surname is {self.first_name} {self.last_name}, "
            f"son of {self.father_name}. I was born in {self.birthday_date}. "
            f"I study in course {self.course_number}, group {self.group_number}. My student ID is {self.student_id}."
        )
    
    def transfer_to_next_course(self) -> None:
        if self.course_number < 5:
            self.course_number += 1
        else:
            print("You are already in the final course.")

student2 = Student("Alice", "Wonderland", "Liddell", "10-10-1999", 3, 1)
print(student2.age)
student2.age += 1
print(student2.age)