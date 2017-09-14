# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        self.result = 0
        self.dfs(root, str(root.val))
        return self.result

    def dfs(self, root, strs):
        if root.left == None and root.right == None:
            self.result += int(strs)
            return
        if root.left != None:
            self.dfs(root.left, strs + str(root.left.val))
        if root.right != None:
            self.dfs(root.right, strs + str(root.right.val))
        return