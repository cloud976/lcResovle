# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from binarytree import BinaryTree

class Solution(object):
    def __init__(self):
        self.sumary = 0
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.mapTree(root, False)
        return self.sumary

    def mapTree(self, treeNode, add):
        if treeNode == None:
            return
        if add and treeNode.left == None and treeNode.right == None:
            self.sumary += treeNode.val
        if treeNode.left != None:
            self.mapTree(treeNode.left, True)
        if treeNode.right != None:
            self.mapTree(treeNode.right, False)

bt = BinaryTree([0,2,4,1,None,3,-1,5,1,None,None,None,6,None,8])
so = Solution()
print so.sumOfLeftLeaves(bt.root)