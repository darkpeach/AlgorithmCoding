# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return None
        slowPtr = head.next
        fastPtr = head.next.next
        while slowPtr and fastPtr:
            if slowPtr == fastPtr:
                break
            if fastPtr.next:
                slowPtr = slowPtr.next
                fastPtr = fastPtr.next.next
            else:
                return None
        if fastPtr == None:
            return None
        slowPtr = head
        while slowPtr != fastPtr:
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next
        return slowPtr
