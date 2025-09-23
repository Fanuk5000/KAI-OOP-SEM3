from abc import ABC, abstractmethod

class AbstractBinaryTree(ABC):
    @abstractmethod
    def insert(self, value):
        pass
    
    @abstractmethod
    def delete(self, value):
        pass

    @abstractmethod
    def search(self, value):
        pass
