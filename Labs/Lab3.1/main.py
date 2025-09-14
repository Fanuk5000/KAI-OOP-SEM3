from painter import Painter
from farmer import Farmer
from student import Student
from file_manager import FileManager
from console_menu import ConsoleMenu

def main():
    file_manager = FileManager("data.txt")
    menu = ConsoleMenu(file_manager)
    menu.run()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")