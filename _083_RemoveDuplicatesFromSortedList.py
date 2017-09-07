# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        ptr = head
        while head and head.next:
            if head.next.val != head.val:
                ptr.next = head.next
                ptr = head.next
            head = head.next
        if ptr:
            ptr.next = None
        return dummy.next