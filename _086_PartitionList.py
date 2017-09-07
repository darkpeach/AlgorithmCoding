# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        less = ListNode(0)
        lessPtr = less
        greater = ListNode(0)
        greaterPtr = greater
        while head:
            if head.val < x:
                lessPtr.next = head
                lessPtr = head
            else:
                greaterPtr.next = head
                greaterPtr = head

            head = head.next
        greaterPtr.next = None
        lessPtr.next = greater.next
        return less.next
