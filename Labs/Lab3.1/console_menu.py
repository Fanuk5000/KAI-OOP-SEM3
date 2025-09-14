from file_manager import FileManager
from student import Student
from painter import Painter
from farmer import Farmer
import regex as re
from os import remove, path

class ConsoleMenu:
    PATTERN_DATE = r"^(?:0[1-9]|[12][0-9]|3[01])-(?:0[1-9]|1[0-2])-\d{4}$"
    

    def __init__(self, file_manager: FileManager):
        self.file_manager = file_manager
        self.objects = []

    def __check_date(self, date_str):
        return re.match(ConsoleMenu.PATTERN_DATE, date_str) is not None

    def run(self):
        while True:
            print("\n1. Add Student\n2. Add Painter\n3. Add Farmer\n4. Save to file\n5. Load from file\n6. Count 2nd course students\n0. Exit")
            choice = input("Choose: ")

            if choice == "1":
                fn = input("First name: ")
                ln = input("Last name: ")
                course = int(input("Course: "))
                bd = input("Birth date (DD-MM-YYYY): ")
                id_exist = input("Student ID exists (y/n): ").lower() == 'y'

                if not self.__check_date(bd):
                    print("Invalid date format. Please use DD-MM-YYYY.")
                    continue

                self.objects.append(Student(fn, ln, course, bd, id_exist))

            elif choice == "2":
                fn = input("First name: ")
                ln = input("Last name: ")
                bd = input("Birth date (DD-MM-YYYY): ")

                if not self.__check_date(bd):
                    print("Invalid date format. Please use DD-MM-YYYY.")
                    continue
                paint_style = input("Painting style: ")

                self.objects.append(Painter(fn, ln, bd, paint_style))

            elif choice == "3":
                fn = input("First name: ")
                ln = input("Last name: ")
                bd = input("Birth date (DD-MM-YYYY): ")

                if not self.__check_date(bd):
                    print("Invalid date format. Please use DD-MM-YYYY.")
                    continue
                farm_location = input("Farm location: ")
                self.objects.append(Farmer(fn, ln, bd, farm_location))

            elif choice == "4":
                print(self.objects)
                self.file_manager.save(self.objects)
                print("Saved.")

            elif choice == "5":
                if path.exists(self.file_manager.filename):
                    self.objects = self.file_manager.load()
                    print("Loaded:")
                    for obj in self.objects:
                        print(f"I am {obj.__class__.__name__}", obj.person_info())
                else:
                    print("No saved data found.")

            elif choice == "6":
                count = sum(
                    1 for obj in self.objects
                    if isinstance(obj, Student) and obj.course == 2
                    and obj.birthday_date.split("-")[1] in ('12', '01', '02')  # Winter months
                )
                print(f"Students on 2nd course: {count}")

            elif choice == "0":
                remove(self.file_manager.filename)
                print("Exiting...")
                break