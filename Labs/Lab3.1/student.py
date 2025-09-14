from person import Person

class Student(Person):
    def __init__(self, firstname: str, lastname: str, course: int, birthday_date: str, student_id_exist: bool = False) -> None:
        super().__init__(firstname, lastname, birthday_date)
        self.course = course
        self.student_id_exist = student_id_exist

    def student_info(self):
        id_status = "have" if self.student_id_exist else "do not have"
        return f"{super().person_info()} I am studying at {self.course} course and I {id_status} a student ID."

    @staticmethod
    def swim():
        print("The student is swimming.")
