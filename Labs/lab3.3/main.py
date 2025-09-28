from BLL.entity_service import EntityService
from PL.menu import Menu

def main():
    service = EntityService()
    menu = Menu(service)
    menu.main_menu()

if __name__ == "__main__":
    main()