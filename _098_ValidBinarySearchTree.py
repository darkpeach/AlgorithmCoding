# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        result = self.checkRoot(root, (1<<31), -(1<<31)-1)
        return result
    def checkRoot(self, root, maxValue, minValue):
        if root.left == None:
            checkLeft = True
        else:
            checkLeft = self.checkRoot(root.left, root.val, minValue) and (root.left.val < root.val and root.left.val > minValue)
        if root.right == None:
            checkRight = True
        else:
            checkRight = self.checkRoot(root.right, maxValue, root.val) and (root.right.val > root.val and root.right.val < maxValue)
        if checkLeft and checkRight:
            return True
        else:
            return False
