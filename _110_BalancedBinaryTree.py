# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        result, height = self.validate(root)
        return result

    def validate(self, root):
        if root == None:
            return True, 0
        else:
            balance, leftHeight = self.validate(root.left)
            if not balance:
                return False, 0
            balance, rightHeight = self.validate(root.right)
            if not balance:
                return False, 0

            return abs(leftHeight - rightHeight) <= 1, max(rightHeight, leftHeight) + 1