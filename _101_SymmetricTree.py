# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        workList = [root]
        while workList:
            listLen = len(workList)
            tempFront = []
            tempBack = []
            for i in range(listLen // 2 + 1):
                if workList[i] == None and workList[listLen - i - 1] == None:
                    continue
                elif workList[i] == None or workList[listLen - i - 1] == None:
                    return False
                elif workList[i].val != workList[listLen - i - 1].val:
                    return False
                else:
                    tempFront.append(workList[i].left)
                    tempFront.append(workList[i].right)
                    tempBack.append(workList[listLen - i - 1].right)
                    tempBack.append(workList[listLen - i - 1].left)
            tempBack.reverse()
            workList = list(tempFront + tempBack)
            tempFront = []
            tempBack = []
        return True

####################### Recursive solution ###########################################
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
            return self.help(root.left, root.right)
        else:
            return True

    def help(self, p, q):
        if p == None and q == None:
            return True
        elif p == None or q == None:
            return False
        elif p.val != q.val:
            return False
        else:
            return self.help(p.left, q.right) and self.help(p.right, q.left)

