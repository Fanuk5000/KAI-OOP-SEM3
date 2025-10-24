from DAL.file_manipulation import JsonManager, BinaryManager, XMLManager, DeserializerFactory
from Entities.student import Student
from os import path

class EntityService:
    def __init__(self):
        self.filename = "students."

    def add_entity(self, student: Student, entity_mode: str = "json") -> None:
        """Add a new student to the file."""
        current_filename = self.filename + entity_mode
        file_manager = DeserializerFactory.get_file_manager(entity_mode, current_filename)
        if path.exists(current_filename):
            students = file_manager.deserialize()
        else:
            students = []
        
        if isinstance(students, list):
            students.append(student)
        file_manager.serialize(students)

    def remove_entity(self, student_id: str, entity_mode: str = "json") -> None:
        """Remove a student by their ID."""
        current_filename = self.filename + entity_mode
        file_manager = DeserializerFactory.get_file_manager(entity_mode, current_filename)
        students = file_manager.deserialize()
        students = [student for student in students if student.student_id != student_id]
        file_manager.serialize(students)

    def read_from_file(self, entity_mode: str = "json") -> list[Student] | tuple[Student, ...]:
        """Read all students from the file."""
        current_filename = self.filename + entity_mode
        file_manager = DeserializerFactory.get_file_manager(entity_mode, current_filename)
        students = file_manager.deserialize()
        return students

    def search_entity(self, student_id: str, entity_mode: str = "json") -> Student | None:
        """Search for a student by their ID."""
        students = self.read_from_file(entity_mode)
        for student in students:
            if student.student_id == student_id:
                return student
        return None

    def find_2_course_who_born_in_winter(self, entity_mode: str = "json") -> list[Student]:
        """Find students in their 2nd course who were born in winter months."""
        winter_months = {12, 1, 2}
        students: list[Student] | tuple[Student, ...] = self.read_from_file(entity_mode)

        suitable_students: list[Student] = []
        for student in students:
            student_birthday_month = int(student.birthday_date.split("-")[1]) # Extract month from DD-MM-YYYY
            if student.course_number == 2 and student_birthday_month in winter_months:
                suitable_students.append(student)
        return suitable_students
    
    def increase_age_when_birthday(self, current_date: str, entity_mode: str = "json") -> None:
        """Increase age of students whose birthday is today."""
        students: list[Student] = list(self.read_from_file(entity_mode))  # Ensure the result is a list
        current_filename = self.filename + entity_mode
        file_manager = DeserializerFactory.get_file_manager(entity_mode, current_filename)
        for student in students:
            student_day_month = student.birthday_date[0:5]  # Extract DD-MM from DD-MM-YYYY
            if student_day_month ==  current_date:
                student.age += 1
                print(f"Happy Birthday {student.first_name} {student.last_name}! You are now {student.age} years old.")
        file_manager.serialize(students)
