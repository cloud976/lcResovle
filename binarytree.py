# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x, left, right):
        self.val = x
        self.left = left
        self.right = right

class BinaryTree(object):
    def __init__(self, lst):
        lstLen = len(lst)
        self.lst = lst
        self.len = lstLen
        self._initNode(0)
        
    def _initNode(self,i):
        if i >= self.len:
            node = None
        elif self.lst[i] == None:
            node = None
        else:
            node = TreeNode(self.lst[i], self._initNode(i*2+1), self._initNode(i*2+2))
        if i == 0 and self.lst[i] != None:
            self.root = node
        return node
        
            