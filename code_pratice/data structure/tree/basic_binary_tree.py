class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def in_order(tree):
    if not tree:
        return
    if tree.left:
        in_order(tree.left)
    
    print(tree.data)

    if tree.right:
        in_order(tree.left)

    return

def pre_order(tree):
    if not tree:
        return

    print(tree.data)

    if tree.left:
        pre_order(tree.left)

    if tree.right:
        pre_order(tree.right)

    return

def post_order(tree):
    if not tree:
        return
    
    if tree.left:
        post_order(tree.left)

    if tree.right:
        post_order(tree.right)

    print(tree.data)

    return

def tree_depth(tree):
    if not tree:
        return 0
    else:
        left_depth = tree_depth(tree.left)
        right_depth = tree_depth(tree.right)
        if left_depth > right_depth:
            return left_depth + 1
        else:
            return right_depth + 1


if __name__ == "__main__":
    tree = Node(1)
    tree.left = Node(2)
    tree.right = Node(3)
    tree.left.left = Node(4)
    tree.left.right = Node(5)
    tree.left.right.left = Node(6)
    tree.right.left = Node(7)
    tree.right.left.left = Node(8)
    tree.right.left.left.right = Node(9)

    print('in order')
    in_order(tree)

    print('pre order')
    pre_order(tree)

    print('post order')
    post_order(tree)

    print('tree depth: ',tree_depth(tree))
        
    