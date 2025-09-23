from abc import ABC, abstractmethod

class AbstractBinaryTree(ABC):
    @abstractmethod
    def insert(self, value):
        pass
    
