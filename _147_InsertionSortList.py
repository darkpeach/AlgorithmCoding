# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        while head:
            ptr = dummy
            while ptr.next != None and head.val > ptr.next.val:
                ptr = ptr.next
            nextHead = head.next
            head.next = ptr.next
            ptr.next = head
            head = nextHead
        return dummy.next