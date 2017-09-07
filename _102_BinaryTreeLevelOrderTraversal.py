# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        result = []
        workList = [root]
        while workList:
            temp = []
            tempRec = []
            for item in workList:
                tempRec.append(item.val)
                if item.left != None:
                    temp.append(item.left)
                if item.right != None:
                    temp.append(item.right)
            workList = temp
            result.append(tempRec)
        return result