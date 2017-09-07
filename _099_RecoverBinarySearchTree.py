# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """

        self.prePtr = TreeNode(-(1 << 31))
        self.firstWrong, self.secondWrong = None, None
        self.traverse(root)
        temp = self.firstWrong.val
        self.firstWrong.val = self.secondWrong.val
        self.secondWrong.val = temp
        return

    def traverse(self, node):
        if node == None:
            return
        else:
            self.traverse(node.left)
            # do something
            if self.firstWrong == None and node.val < self.prePtr.val:
                self.firstWrong = self.prePtr
            if self.firstWrong != None and node.val < self.prePtr.val:
                self.secondWrong = node
            self.prePtr = node
            self.traverse(node.right)