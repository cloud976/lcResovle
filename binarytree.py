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
        else:
            self.root = TreeNode(lst[0], None, None)
        for i in range(1, lstLen):
            if lst[i] != None:
                treeNode = TreeNode(lst[i], None, None)
                if i*2<lstLen and lst[i*2]!=None:
                    treeNode.left = TreeNode(lst[i*2], None, None)
                if i*2+1<lstLen and lst[i*2+1]!=None:
                    treeNode.right = TreeNode(lst[i*2+1], None, None)
            
                    
bt = BinaryTree([1,2,3,4,5,6])
print bt.root
