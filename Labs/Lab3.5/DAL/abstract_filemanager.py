from abc import ABC, abstractmethod
from Entities.student import Student

class ABCFileManager(ABC):
    @abstractmethod
    def serialize(self, students: list[Student]) -> None:
        pass

    @abstractmethod
    def deserialize(self) -> list[Student]:
        pass