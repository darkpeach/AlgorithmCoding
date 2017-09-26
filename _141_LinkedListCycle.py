# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False
        slowPtr = head.next
        fastPtr = head.next.next
        while slowPtr and fastPtr:
            if slowPtr == fastPtr:
                return True
            if fastPtr.next:
                slowPtr = slowPtr.next
                fastPtr = fastPtr.next.next
            else:
                return False
        return False
