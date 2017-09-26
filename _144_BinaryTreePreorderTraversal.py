# Simple recursive solution
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        def myPreorderTraversal(root, result):
            if root == None:
                return
            result.append(root.val)
            myPreorderTraversal(root.left, result)
            myPreorderTraversal(root.right, result)

        if not root:
            return []
        result = []
        myPreorderTraversal(root, result)
        return result
# none recursive solution ( Morris Traversal)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        curr = root
        result = []
        while curr:
            if curr.left == None:
                result.append(curr.val)
                curr = curr.right
            else:
                preCurr = curr.left
                while preCurr.right and preCurr.right != curr:
                    preCurr = preCurr.right
                if preCurr.right != curr:
                    result.append(curr.val)
                    preCurr.right = curr
                    curr = curr.left
                else:
                    preCurr.right = None
                    curr = curr.right
        return result
