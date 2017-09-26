#recursive solution
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        def myPostorderTraversal(root, result):
            if root == None:
                return
            myPostorderTraversal(root.left, result)
            myPostorderTraversal(root.right, result)
            result.append(root.val)

        result = []
        if not root:
            return []
        else:
            myPostorderTraversal(root, result)
            return result

# Morris Traversal
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        def dump(fromNode, toNode, result):
            temp = []
            while fromNode != toNode:
                temp.append(fromNode.val)
                fromNode = fromNode.right
            temp.append(fromNode.val)
            while temp != []:
                result.append(temp.pop())
            return

        dummy = TreeNode(0)
        dummy.left = root
        curr = dummy
        result = []
        while curr:
            if curr.left == None:
                curr = curr.right
            else:
                preCurr = curr.left
                while preCurr.right and preCurr.right != curr:
                    preCurr = preCurr.right
                if preCurr.right == None:
                    preCurr.right = curr
                    curr = curr.left
                else:
                    preCurr.right = None
                    dump(curr.left, preCurr, result)
                    curr = curr.right
        return result