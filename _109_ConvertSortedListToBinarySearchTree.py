# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        elif not head.next:
            return TreeNode(head.val)
        elif not head.next.next:
            tree = TreeNode(head.next.val)
            tree.left = TreeNode(head.val)
            return tree
        else:
            firstPtr = head
            secondPtr = head.next.next
            while secondPtr.next and secondPtr.next.next:
                firstPtr = firstPtr.next
                secondPtr = secondPtr.next.next
            temp = firstPtr.next
            result = TreeNode(temp.val)
            firstPtr.next = None
            result.left = self.sortedListToBST(head)
            result.right = self.sortedListToBST(temp.next)
            return result