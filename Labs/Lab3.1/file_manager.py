from person import Person
from student import Student
from painter import Painter
from farmer import Farmer
import json

class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def save(self, objects):
        with open(self.filename, 'w') as file:
            for obj in objects:
                typename = obj.__class__.__name__
                name = obj.firstname + obj.lastname
                data = obj.__dict__
                file.write(f"{typename} {name}\n")
                file.write(json.dumps(data, ensure_ascii=False, indent=2))
                file.write(";\n")
    
    def load(self):
        objects = []
        with open(self.filename, "r", encoding="utf-8") as f:
            content = f.read().strip().split(";\n")
            for block in content:
                if not block.strip() or block == '':
                    continue
                header, json_part = block.split("\n", 1)
                typename, _ = header.split(" ", 1)
                print("Json part:", json_part, repr(json_part), "typename:", typename)  # Debugging line
                data = json.loads(json_part.strip(';\n'))
                if typename == "Student":
                    obj = Student(**data)
                elif typename == "Painter":
                    obj = Painter(**data)
                elif typename == "Farmer":
                    obj = Farmer(**data)
                else:
                    continue
                objects.append(obj)
        return objects