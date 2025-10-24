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
            CHOOSE_COMMANDS:dict = {
                1: "Add Entity",
                2: "Remove Entity",
                3: "Search Entity",
                4: "Clear a File",
                5: "Print students of 2-nd course and who born in winter",
                6: "Increase age if today birthday",
                7: "Get driver license if person suitable",
                8: "Exit",
            }
            for key, value in CHOOSE_COMMANDS.items():
                print(f"{key}. {value}")

            choice = int(input("Enter your choice: "))
            if choice not in CHOOSE_COMMANDS:
                print("Invalid choice. Please try again.")
                continue

            COMMANDS = [self.add_entity,
                        self.remove_entity, 
                        self.search_entity, 
                        clear_file, 
                        self.exit_program,
                        self.service.find_2_course_who_born_in_winter,
                        self.service.increase_age_when_birthday]
            ACTIONS = dict([(str(i + 1), COMMANDS[i]) for i in range(len(COMMANDS))])

            for key, value in ACTIONS.items():
                if choice == key:
                    result = ACTIONS[key]()
                    if result == "Govno_vveli":
                        problem_in_commands = True
                        break
            else:
                problem_in_commands = False
            
            if problem_in_commands:
                continue
                

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

    def remove_entity(self) -> str | None:
        entity_id = input("Enter ID to remove: ")
        entity_mode = input("Enter mode (json, xml, bin): ")

        if entity_mode not in {"json", "xml", "bin"}:
            print("Invalid mode. Please choose from json, xml, or bin.")
            return "Govno_vveli"
        
        self.service.remove_entity(entity_id, entity_mode)

    def search_entity(self) -> None:
        entity_id = input("Enter ID to search: ")
        entity_mode = input("Enter mode (json, xml, bin): ")
        entity = self.service.search_entity(entity_id, entity_mode)
        if entity:
            print(f"Entity found: {entity.student_info()}")
        else:
            print("Entity not found.")
    
    def exit_program(self) -> None:
        JSON_FILENAME, BINARY_FILENAME, XML_FILENAME = "students.json", "students.bin", "students.xml"
        del_if_exists({JSON_FILENAME, BINARY_FILENAME, XML_FILENAME})
        exit(0)

    def clear_the_file(self) -> None:
        input_filename = input("Enter filename to clear(students.json, students.bin, students.xml): ")
        clear_file(input_filename)

    def find_2_course_who_born_in_winter(self) -> None:
        entity_mode = input("Enter mode (json, xml, bin): ")
        students = self.service.find_2_course_who_born_in_winter(entity_mode)
        for student in students:
            print(student.student_info())

    def increase_age_when_birthday(self) -> None:
        entity_mode = input("Enter mode (json, xml, bin): ")
        self.service.increase_age_when_birthday(entity_mode)

    def __check_file_mode(self, mode: str) -> bool:
        return mode in {"json", "xml", "bin"}
    