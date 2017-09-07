# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        result = []
        workList = [root]
        flag = 1
        while workList:
            temp = []
            tempRes = []
            for item in workList:
                tempRes.append(item.val)
                if item.left:
                    temp.append(item.left)
                if item.right:
                    temp.append(item.right)
            workList = temp
            if flag < 0:
                tempRes.reverse()
            flag = flag * -1
            result.append(tempRes)
        return result