from abstract_tree import AbstractBinaryTree
from collections import deque

class BinaryTree(AbstractBinaryTree):
    class Node:
        def __init__(self, value):
            self.value = value
            self.left: BinaryTree.Node | None = None
            self.right: BinaryTree.Node | None = None
        
        def __repr__(self):
            return f"Node({self.value})"

    def __init__(self, value=None):
        self.root = self.Node(value)

    def insert(self, value):
        if self.root.left is None:
            self.root.left = self.Node(value)
        elif self.root.right is None:
            self.root.right = self.Node(value)
        else:
            self._logical_insert(self.root, value)

    # Preorder logic insertion
    def _logical_insert(self, node: Node, value):
        
        queue = deque([node])

        while queue:
            temp = queue.popleft()
            
            if temp.left is None:
                temp.left = self.Node(value)
                return
            else:
                queue.append(temp.left)
            
            if temp.right is None:
                temp.right = self.Node(value)
                return
            else:
                queue.append(temp.right)
    
    # Analog of IComparable<T> in C#
    def __lt__(self, other: "BinaryTree") -> bool:
        """
        Compare two binary trees based on the sum of their node values.
        """
        if not isinstance(other, BinaryTree):
            raise TypeError("Can only compare BinaryTree objects")

        def tree_sum(node: BinaryTree.Node) -> int:
            if node is None:
                return 0
            return node.value + tree_sum(node.left) + tree_sum(node.right)

        return tree_sum(self.root) < tree_sum(other.root)
        
 
    # IEnumerable: allow "for x in tree"
    def __iter__(self):
        return self._inorder(self.root)

    # IEnumerator: recursive generator
    def _inorder(self, node: Node | None):
        if node:
            yield from self._inorder(node.left)   # Left
            yield node.value                      # Root
            yield from self._inorder(node.right)  # Right
