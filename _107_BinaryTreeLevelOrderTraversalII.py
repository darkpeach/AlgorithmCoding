# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        startList = [root]
        result = []
        while startList:
            temp = []
            tempRes = []
            for item in startList:
                tempRes.append(item.val)
                if item.left:
                    temp.append(item.left)
                if item.right:
                    temp.append(item.right)
            result.append(tempRes)
            startList = temp
        result.reverse()
        return result
