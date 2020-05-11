class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class InorderTraversal:
    def inorder_traversal(self, root):
        res = list()
        self.helper(root, res)
        return res

    def helper(self, root, res):
        if root:
            if root.left:
                self.helper(root.left, res)
            res.append(root.val)
            if root.right:
                self.helper(root.right, res)