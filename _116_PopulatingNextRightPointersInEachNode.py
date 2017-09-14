# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root == None:
            return
        rootList = [root]
        while rootList != []:
            tempList = []
            for i in range(len(rootList)):
                if i != len(rootList) - 1:
                    rootList[i].next = rootList[i + 1]
                else:
                    rootList[i].next = None
                if rootList[i].left != None:
                    tempList.append(rootList[i].left)
                if rootList[i].right != None:
                    tempList.append(rootList[i].right)
            rootList = tempList
        return