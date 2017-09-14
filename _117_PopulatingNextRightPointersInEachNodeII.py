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
        parent = root
        parent.next = None
        while parent != None:
            last, first = None, None
            while parent != None:
                for node in [parent.left, parent.right]:
                    if node != None:
                        if last == None:
                            first = node
                        else:
                            last.next = node
                        last = node
                parent = parent.next
            parent = first
        return