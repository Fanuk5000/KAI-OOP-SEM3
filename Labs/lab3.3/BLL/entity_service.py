from DAL.file_manipulation import serialize_to_file, deserialize_from_file
from Entities.student import Student
from os import path

class EntityService:
    def __init__(self):
        self.filename = "students."

    def add_entity(self, student: Student, entity_mode: str = "json") -> None:
        """Add a new student to the file."""
        current_filename = self.filename + entity_mode
        if path.exists(current_filename):
            students = deserialize_from_file(current_filename, mode=entity_mode)
        else:
            students = []
        
        if isinstance(students, list):
            students.append(student)
        elif isinstance(students, tuple):
            students = list(students) + [student]
        serialize_to_file(students, current_filename, mode=entity_mode)

    def remove_entity(self, student_id: str, entity_mode: str = "json") -> None:
        """Remove a student by their ID."""
        current_filename = self.filename + entity_mode
        students = deserialize_from_file(current_filename, mode=entity_mode)
        students = [student for student in students if student.student_id != student_id]
        serialize_to_file(students, current_filename, mode=entity_mode)

    def search_entity(self, student_id: str, entity_mode: str = "json") -> Student | None:
        """Search for a student by their ID."""
        current_filename = self.filename + entity_mode
        students = deserialize_from_file(current_filename, mode=entity_mode)
        for student in students:
            if student.student_id == student_id:
                return student
        return None

    def get_all_entities(self) -> list[Student]:
        """Retrieve all students."""
        return deserialize_from_file(self.filename, mode=self.mode)