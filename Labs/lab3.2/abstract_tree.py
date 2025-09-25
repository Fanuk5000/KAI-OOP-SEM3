from abc import ABC, abstractmethod

class AbstractBinaryTree(ABC):
    @abstractmethod
    def insert(self, value):
        pass
    
    @abstractmethod
    def _logical_insert(self, node, value):
        pass

    @abstractmethod
    def _inorder(self, node: None):
        pass
