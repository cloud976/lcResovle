# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left, right):
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None:
            return False
        for lst in self.listAllPath(root):
            if sum == reduce(lambda x,y: x+y, lst):
                return True
        return False
    def listAllPath(self, root):
        pathList = []
        if root.left != None:
            for path in self.listAllPath(root.left):
                pathList.append([root.val] + path)
        if root.right != None:
             for path in self.listAllPath(root.right):
                pathList.append([root.val] + path)
        if  root.left == None and root.right == None:
            pathList.append([root.val])
        return pathList

so = Solution()
root = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7, None, None), TreeNode(2, None, None)), None), TreeNode(8, TreeNode(13, None, None), TreeNode(4, None, TreeNode(1, None, None))))
print(so.hasPathSum(root, 26))