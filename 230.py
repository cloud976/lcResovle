# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left, right):
        self.val = x
        self.left = TreeNode(left, None, None) if ((type(left) != TreeNode) and (left != None)) else left
        self.right = TreeNode(right, None, None) if ((type(right) != TreeNode) and (right != None)) else right

class Solution(object):
    def __init__(self):
        self.treeList = []
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.mapTree(root, k)
        return self.treeList.pop()
        
    def mapTree(self, root, k):
        if root != None:
            self.mapTree(root.left, k)
            if len(self.treeList) >= k:
                return
            self.treeList.append(root.val)
            self.mapTree(root.right, k)

so = Solution();
bst = TreeNode(1, None, None)
print so.kthSmallest(bst, 1)