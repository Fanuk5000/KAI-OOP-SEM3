import pickle
from os import path
from Entities.student import Student
import json
import xml.etree.ElementTree as ET
from xml.dom.minidom import parseString

def to_xml(student: dict) -> ET.Element:
    student_element = ET.Element("student")
    for key, value in student.items():
        ET.SubElement(student_element, key).text = str(value)
    return student_element

def clear_file(filename: str) -> None:
    with open(filename, "w", encoding="utf-8"):
        pass

# Serialize an array of Student objects into a file
def serialize_to_file(students: list[Student], filename: str, mode: str = "json") -> None:
    # Convert each Student object to a dictionary
    couple_students:list = [student.__dict__ for student in students]
    if mode == "json":
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(couple_students, file, indent=4)
    elif mode == "bin":
        with open(filename, "wb") as file:
            pickle.dump(couple_students, file)
    elif mode == "xml":
        root = ET.Element("Students")
        for student in couple_students:
            root.append(to_xml(student))

        # Convert to a string and pretty print
        xml_string = ET.tostring(root, encoding="utf-8")
        pretty_xml = parseString(xml_string).toprettyxml(indent="  ")

        # Write the pretty XML to a file
        with open(filename, "w", encoding="utf-8") as file:
            file.write(pretty_xml)

def deserialize_from_file(filename: str, set_mode: bool = False, mode: str = "json") -> list[Student] | tuple[Student, ...]:
    if mode == "json":
        with open(filename, "r", encoding="utf-8") as file:
            students_dicts = json.load(file)
            if set_mode:
                return tuple(Student(**student_dict) for student_dict in students_dicts)
            else:
                return [Student(**student_dict) for student_dict in students_dicts]
    elif mode == "bin":
        with open(filename, "rb") as file:
            students_dicts = pickle.load(file)
            
            return [Student(**student_dict) for student_dict in students_dicts]
    elif mode == "xml":
        tree = ET.parse(filename)
        root = tree.getroot()
        students_dicts = []
        for student_elem in root.findall("student"):
            student_dict = {child.tag: child.text for child in student_elem}
            students_dicts.append(student_dict)
        return [Student(**student_dict) for student_dict in students_dicts]
