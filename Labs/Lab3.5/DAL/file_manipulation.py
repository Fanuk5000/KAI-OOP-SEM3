import pickle
from os import path
from Entities.student import Student
import json
import xml.etree.ElementTree as ET
from xml.dom.minidom import parseString
from DAL.abstract_filemanager import ABCFileManager

class JsonManager(ABCFileManager):
    def __init__(self, filename: str):
        self.__filename = filename

    def serialize(self, students: list[Student]) -> None:
        couple_students:list = [student.__dict__ for student in students]
        with open(self.__filename, "w", encoding="utf-8") as file:
            json.dump(couple_students, file, indent=4)

    def deserialize(self) -> list[Student]:
        with open(self.__filename, "r", encoding="utf-8") as file:
            students_dicts = json.load(file)
        return [Student(**student_dict) for student_dict in students_dicts]

class BinaryManager(ABCFileManager):
    def __init__(self, filename: str):
        self.__filename = filename

    def serialize(self, students: list[Student]) -> None:
        couple_students:list = [student.__dict__ for student in students]
        with open(self.__filename, "wb") as file:
            pickle.dump(couple_students, file)

    def deserialize(self) -> list[Student]:
        with open(self.__filename, "rb") as file:
            students_dicts = pickle.load(file)
            return [Student(**student_dict) for student_dict in students_dicts]
        
class XMLManager(ABCFileManager):
    def __init__(self, filename: str):
        self.__filename = filename

    def serialize(self, students: list[Student]) -> None:
        couple_students:list = [student.__dict__ for student in students]
        root = ET.Element("Students")
        for student in couple_students:
            root.append(self.__to_xml(student))

        # Convert to a string and pretty print
        xml_string = ET.tostring(root, encoding="utf-8")
        pretty_xml = parseString(xml_string).toprettyxml(indent="  ")

        # Write the pretty XML to a file
        with open(self.__filename, "w", encoding="utf-8") as file:
            file.write(pretty_xml)

    def deserialize(self) -> list[Student]:
        tree = ET.parse(self.__filename)
        root = tree.getroot()
        students_dicts = []
        for student_elem in root.findall("student"):
            student_dict = {child.tag: child.text for child in student_elem}
            students_dicts.append(student_dict)
        return [Student(**student_dict) for student_dict in students_dicts]
    
    @staticmethod
    def __to_xml(student: dict) -> ET.Element:
        student_element = ET.Element("student")
        for key, value in student.items():
            ET.SubElement(student_element, key).text = str(value)
        return student_element

def clear_file(filename: str) -> None:
    with open(filename, "w", encoding="utf-8"):
        pass

class DeserializerFactory:
    @staticmethod
    def get_file_manager(mode: str, filename: str) -> ABCFileManager:
        if mode == "json":
            return JsonManager(filename)
        elif mode == "bin":
            return BinaryManager(filename)
        elif mode == "xml":
            return XMLManager(filename)
        else:
            raise ValueError(f"Unsupported deserialization mode: {mode}")