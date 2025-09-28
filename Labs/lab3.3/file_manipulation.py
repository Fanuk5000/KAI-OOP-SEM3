import pickle
from os import path
from student import Student
import json

# Serialize an array of Student objects into a file
def serialize_to_file(students: list[Student], filename: str, mode: str = "json") -> None:
    """
    Serializes a list of Student objects to a file in the specified format.

    Args:
        students (list[Student]): A list of Student objects to be serialized.
        filename (str): The name of the file to which the data will be written.
        mode (str, optional): The serialization format. Supported values are:
            - "json": Serialize the data to a JSON file (default).
            - "pickle": Serialize the data to a binary file using pickle.

    Returns:
        None

    Raises:
        ValueError: If the specified mode is not "json" or "pickle".
        TypeError: If the students list contains non-Student objects.
        IOError: If there is an error writing to the file.
    """
    # Convert each Student object to a dictionary
    couple_students:list = [student.__dict__ for student in students]
    if mode == "json":
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(couple_students, file, indent=4)
    elif mode == "pickle":
        with open(filename, "wb") as file:
            pickle.dump(couple_students, file)

def deserialize_from_file(filename: str, set_mode: bool = False, mode: str = "json") -> list[Student] | tuple[Student, ...]:
    """
    Deserializes a file into a list or tuple of Student objects based on the specified mode.

    Args:
        filename (str): The name of the file to read from.
        set_mode (bool, optional): If True, returns a tuple of Student objects. Defaults to False.
        mode (str, optional): The deserialization format. Supported values are:
                        return [Student(**student_dict) for student_dict in students_dicts]
                else:
                    raise ValueError(f"Unsupported mode: {mode}. Supported modes are 'json' and 'pickle'.")
            - "pickle": Deserialize from a binary file using pickle.

    Returns:
        list[Student] | tuple[Student, ...]: A list or tuple of Student objects.

    Raises:
        ValueError: If the specified mode is not "json" or "pickle".
        IOError: If there is an error reading from the file.
    """
    if mode == "json":
        with open(filename, "r", encoding="utf-8") as file:
            students_dicts = json.load(file)
            clear_file(filename)
            if set_mode:
                return tuple(Student(**student_dict) for student_dict in students_dicts)
            else:
                return [Student(**student_dict) for student_dict in students_dicts]
    elif mode == "pickle":
        with open(filename, "rb") as file:
            students_dicts = pickle.load(file)
            clear_file(filename)
            
            return [Student(**student_dict) for student_dict in students_dicts]

def clear_file(filename: str) -> None:
    with open(filename, "w", encoding="utf-8"):
        pass