# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        result = []
        if root:
            stack.append(root)
        while stack != []:
            if type(stack[-1]) == int:
                result.append(stack.pop())
                continue
            newNode = stack.pop()
            print(newNode)
            if newNode.right:
                stack.append(newNode.right)
            stack.append(newNode.val)
            if newNode.left:
                stack.append(newNode.left)
        return result
############# Morris Traversal
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        while root != None:
            if root.left == None:
                result.append(root.val)
                root = root.right
            else:
                temp = root.left
                curr = root.left
                while curr.right != None:
                    curr = curr.right
                curr.right = root
                root.left = None
                root = temp

        return result