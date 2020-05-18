class Node(object):
    
    def __init__(self, data, parent):
        self.left = None
        self.right = None
        self.value = data
        self.parent = parent

    
class BinarySearchTree(object):
    
    def __init__(self, root):
        self.root = root

    def empty(self):
        return self.root == None

    def __insert(self, value):
        new_node = Node(value, None)

        if self.empty():
            self.root = new_node
        else:
            parent_node = self.root
            while True:
                
                if value < parent_node.value:
                    if parent_node.left is None:
                        parent_node.left = new_node
                        break
                    else:
                        parent_node = parent_node.left
                else:
                    if parent_node.right is None:
                        parent_node.right = new_node
                        break
                    else:
                        parent_node = parent_node.right
            new_node.parent = parent_node

    def insert(self, *values):
        for value in values:
            self.insert(value)
        return self

    def search(self, value):
        if self.empty():
            raise IndexError('Warning: trere is empty')
        else:
            node = self.root
            while node is not None and node.value != value:
                node = node.left if node.value > value else node.right
        return node

    def get_max(self, node=None):
        if node is None:
            return self.root
        if not self.empty():
            while node.rigth is not None:
                node = node.right
        return node

    def get_min(self, node=None):
        if node is None:
            return self.root

        if not self.empty():
            while node.left is not None:
                node = node.left

        return node



    
                
    
        
    