import json
from student import Student
from os import remove, path
from file_manipulation import serialize_to_file, deserialize_from_file, clear_file

def del_if_exists(filename: set[str]) -> None:
    for file in filename:
        if path.exists(file):
            remove(file)

def print_students(students: list[Student] | tuple[Student, ...]) -> None:
    for student in students:
        print(student.student_info())

def main() -> int:
    JSON_FILENAME = "students.json"
    BINARY_FILENAME = "students.bin"
    del_if_exists({JSON_FILENAME, BINARY_FILENAME})

    students:list[Student] = [
        Student("John", "Doe", "Smith", "01-01-2000", 1, 1),
        Student("Jane", "Roe", "Johnson", "02-02-2001", 2, 2),
        Student("Alice", "Green", "Brown", "03-03-2002", 3, 3),
        Student("Gregory", "Green", "Brown", "03-03-2002", 3, 3)
    ]
    students2:list[Student] = [
        Student("Oliver", "Doe", "Smith", "01-01-2000", 1, 1),
        Student("Jane", "Roe", "Johnson", "02-02-2099", 2, 2),
        Student("Alice", "Oil", "Brown", "03-03-2002", 3, 5),
        Student("Gregory", "Green", "Brown", "03-03-2002", 3, 3)
    ]
    # JSON part ------------------------------------------
    serialize_to_file(students, JSON_FILENAME)
    deserialized_students_tpl: list[Student] | tuple[Student, ...] = deserialize_from_file(JSON_FILENAME, set_mode=True)
    
    serialize_to_file(students2, JSON_FILENAME)
    deserialized_students_lst: list[Student] | tuple[Student, ...] = deserialize_from_file(JSON_FILENAME)

    # Iterate over both collections and compare their Student objects
    for student_tpl, student_lst in zip(deserialized_students_tpl, deserialized_students_lst):
        if student_tpl == student_lst:
            print(f"Match: {student_tpl.first_name} {student_tpl.last_name}")
        else:
            print(f"Mismatch: {student_tpl.first_name} {student_tpl.last_name} != {student_lst.first_name} {student_lst.last_name}")

    # Binary part ------------------------------------------
    serialize_to_file(students, BINARY_FILENAME, mode="pickle")
    deserialized_students_bin: list[Student] | tuple[Student, ...] = deserialize_from_file(BINARY_FILENAME, mode="pickle")
    print_students(deserialized_students_bin)

    # XML part ------------------------------------------
    serialize_to_file(students, "students.xml", mode="xml")
    deserialized_students_xml: list[Student] | tuple[Student, ...] = deserialize_from_file("students.xml", mode="xml")
    print_students(deserialized_students_xml)

    return 0

# Example usage
if __name__ == "__main__":
    main()