# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x, left, right):
        self.val = x
        self.left = left
        self.right = right

class BinaryTree(object):
    def __init__(self, lst):
        lstLen = len(lst)
        if lstLen == 0:
            self.root = None
        self.root = TreeNode(lst[0], None, None)
        for i in range(lstLen):
            