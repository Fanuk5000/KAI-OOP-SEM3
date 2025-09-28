from BLL.entity_service import EntityService
from DAL.file_manipulation import clear_file
from Entities.student import Student
from os import remove, path

def del_if_exists(filename: set[str]) -> None:
    for file in filename:
        if path.exists(file):
            remove(file)

class Menu:
    def __init__(self, service: EntityService):
        self.service = service

    def main_menu(self):
        while True:
            print("1. Add Entity")
            print("2. Remove Entity")
            print("3. Search Entity")
            print("4. Clear a File")
            print("5. Exit")

            choice = input("Enter your choice: ")
            
            if choice == "1":
                result = self.add_entity()
                if result == "Govno_vveli":
                    continue
            elif choice == "2":
                self.remove_entity()
            elif choice == "3":
                self.search_entity()
            elif choice == "4":
                input_filename = input("Enter filename to clear(students.json, students.bin, students.xml): ")
                clear_file(input_filename)
            elif choice == "5":
                JSON_FILENAME = "students.json"
                BINARY_FILENAME = "students.bin"
                XML_FILENAME = "students.xml"
                del_if_exists({JSON_FILENAME, BINARY_FILENAME, XML_FILENAME})

                break

    def add_entity(self):
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        father_name = input("Enter father name: ")
        birthday_date = input("Enter birthday date: ")
        course_number = int(input("Enter course number: "))
        group_number = int(input("Enter group number: "))
        try:
            entity = Student(
                first_name=first_name,
                last_name=last_name,
                father_name=father_name,
                birthday_date=birthday_date,
                course_number=course_number,
                group_number=group_number
            )
        except ValueError:
            print("Invalid date format. Please use DD-MM-YYYY.")
            return "Govno_vveli"
        
        entity_mode = input("Enter mode (json, xml, bin): ")

        if entity_mode not in {"json", "xml", "bin"}:
            print("Invalid mode. Please choose from json, xml, or bin.")
            return "Govno_vveli"

        self.service.add_entity(entity, entity_mode)

    def remove_entity(self):
        entity_id = input("Enter ID to remove: ")
        entity_mode = input("Enter mode (json, xml, bin): ")
        self.service.remove_entity(entity_id, entity_mode)

    def search_entity(self):
        entity_id = input("Enter ID to search: ")
        entity_mode = input("Enter mode (json, xml, bin): ")
        entity = self.service.search_entity(entity_id, entity_mode)
        if entity:
            print(f"Entity found: {entity.student_info()}")
        else:
            print("Entity not found.")