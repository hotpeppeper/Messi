class Node(object):
    
    def __init__(self, data, parent):
        self.left = None
        self.right = None
        self.value = data
        self.parent = parent

    
class BinarySearchTree(object):
    
    def __init__(self, root=None):
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
            self.__insert(value)
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
            node = self.root
        if not self.empty():
            while node.right is not None:
                node = node.right
        return node

    def get_min(self, node=None):
        if node is None:
            node = self.root

        if not self.empty():
            # node = self.root
            while node.left is not None:
                node = node.left

        return node


def binary_search_tree():
    r"""
    Example
                  8
                 / \
                3   10
               / \    \
              1   6    14
                 / \   /
                4   7 13
    >>> t = BinarySearchTree().insert(8, 3, 6, 1, 10, 14, 13, 4, 7)
    >>> print(" ".join(repr(i.value) for i in t.traversal_tree()))
    8 3 1 6 4 7 10 14 13
    >>> print(" ".join(repr(i.value) for i in t.traversal_tree(postorder)))
    1 4 7 6 3 13 14 10 8
    >>> BinarySearchTree().search(6)
    Traceback (most recent call last):
    ...
    IndexError: Warning: Tree is empty! please use another.
    """
    testlist = (8, 3, 6, 1, 10, 14, 13, 4, 7)
    t = BinarySearchTree()
    for i in testlist:
        t.insert(i)

    # Prints all the elements of the list in order traversal
    print(t)

    if t.search(6) is not None:
        print("The value 6 exists")
    else:
        print("The value 6 doesn't exist")

    if t.search(-1) is not None:
        print("The value -1 exists")
    else:
        print("The value -1 doesn't exist")

    if not t.empty():
        print("Max Value: ", t.get_max().value)
        print("Min Value: ", t.get_min().value)

    # for i in testlist:
    #     t.remove(i)
    #     print(t)

if __name__ == "__main__":
    binary_search_tree()
    
                
    
        
    