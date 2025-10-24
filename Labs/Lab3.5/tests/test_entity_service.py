# to run with sys.sdtout -s flag
import pytest
from Entities.student import Student
from BLL.entity_service import EntityService
from os import path

@pytest.fixture
def mock_file_manager():
    """Fixture to provide a mock file manager."""
    class MockFileManager:
        def __init__(self):
            self.data = []

        def deserialize(self):
            return self.data

        def serialize(self, students):
            self.data = students

    return MockFileManager()


@pytest.fixture
def monkeypatched_get_file_manager(monkeypatch, mock_file_manager):
    """Monkeypatch the DeserializerFactory.get_file_manager method."""
    def mock_get_file_manager(entity_mode, filename):
        return mock_file_manager

    monkeypatch.setattr("DAL.file_manipulation.DeserializerFactory.get_file_manager", mock_get_file_manager)

@pytest.fixture
def setup_entity_service(monkeypatched_get_file_manager):
    service = EntityService()
    yield service

def test_add_entity_with_empty_file(setup_entity_service, mock_file_manager):
    """Test add_entity using pytest monkeypatch."""
    service:EntityService = setup_entity_service
    student = Student("Nigeron", "Zelebobr", "Smith", "15-05-2000", 2, 3)
    service.add_entity(student, entity_mode="json")

    # Assert that the mock file manager's serialize method was called with the correct data
    assert student in mock_file_manager.data

def test_add_entity_with_file(setup_entity_service, mock_file_manager, monkeypatch):
    """Test add_entity using pytest monkeypatch."""
    service:EntityService = setup_entity_service
    def mock_path_exists(filepath):
        if filepath == "students.json":
            return True  # Simulate that the file exists
        return False
    
    monkeypatch.setattr(path, "exists", mock_path_exists)
    student = Student("Nigeron", "Zelebobr", "Smith", "15-05-2000", 2, 3)
    mock_file_manager.data = [Student("Zubarev", "Ugana", "Sanchies", "14-12-6666", 2, 3)]
    service.add_entity(student, entity_mode="json")

    # Assert that the mock file manager's serialize method was called with the correct data
    assert student in mock_file_manager.data

def test_remove_entity_with_mock(setup_entity_service, mock_file_manager):
    """Test remove_entity using pytest monkeypatch."""
    service:EntityService = setup_entity_service
    student1 = Student("Nigeron", "Zelebobr", "Smith", "15-05-2000", 2, 3)
    student2 = Student("Alice", "Wonderland", "Liddell", "10-10-1999", 3, 1)
    mock_file_manager.data = [student1, student2]

    service.remove_entity(student1.student_id, entity_mode="json")

    # Assert that the student was removed
    assert mock_file_manager.data == [student2]

def test_read_from_file(setup_entity_service, mock_file_manager):
    service:EntityService = setup_entity_service
    student1 = Student("Nigeron", "Zelebobr", "Smith", "15-05-2000", 2, 3)
    student2 = Student("Alice", "Wonderland", "Liddell", "10-10-1999", 3, 1)
    mock_file_manager.data = [student1, student2]

    assert mock_file_manager.data == service.read_from_file()
    
def test_search_entity_in_file(setup_entity_service, mock_file_manager):
    service:EntityService = setup_entity_service
    student1 = Student("Nigeron", "Zelebobr", "Smith", "15-05-2000", 2, 3)
    student2 = Student("Alice", "Wonderland", "Liddell", "10-10-1999", 3, 1)
    mock_file_manager.data = [student1, student2]

    assert service.search_entity("AWL1010199931") in (mock_file_manager.data)


def test_search_entity_not_in_file(setup_entity_service, mock_file_manager):
    service:EntityService = setup_entity_service
    student1 = Student("Nigeron", "Zelebobr", "Smith", "15-05-2000", 2, 3)
    student2 = Student("Alice", "Wonderland", "Liddell", "10-10-1999", 3, 1)
    mock_file_manager.data = [student1, student2]

    assert service.search_entity("OBS1010199931") not in (mock_file_manager.data)

def test_find_2_course_who_born_in_winter(setup_entity_service, mock_file_manager):
    service:EntityService = setup_entity_service
    student1 = Student("Nigeron", "Zelebobr", "Smith", "15-01-2000", 2, 3)  # Born in winter and 2nd course
    student2 = Student("Alice", "Wonderland", "Liddell", "10-10-1999", 3, 1)
    mock_file_manager.data = [student1, student2]
    suitable_students = service.find_2_course_who_born_in_winter()

    for suit_stud in suitable_students:
        assert suit_stud in mock_file_manager.data

def test_find_2_course_who_born_not_in_winter(setup_entity_service, mock_file_manager):
    service:EntityService = setup_entity_service
    student1 = Student("Nigeron", "Zelebobr", "Smith", "15-05-2000", 2, 3)
    student2 = Student("Alice", "Wonderland", "Liddell", "10-10-1999", 3, 1)
    mock_file_manager.data = [student1, student2]
    suitable_students = service.find_2_course_who_born_in_winter()

    assert suitable_students not in (mock_file_manager.data)

def test_increase_age_when_birthday(setup_entity_service, mock_file_manager):
    service:EntityService = setup_entity_service
    student1 = Student("Nigeron", "Zelebobr", "Smith", "15-05-2000", 2, 3)
    save_student1_age = student1.age
    student2 = Student("Alice", "Wonderland", "Liddell", "10-10-1999", 3, 1)
    save_student2_age = student2.age
    mock_file_manager.data = [student1, student2]
    service.increase_age_when_birthday("15-05")

    assert  student1.age - save_student1_age == 1
    assert  save_student2_age - student2.age == 0