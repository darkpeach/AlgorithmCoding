# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        size = 1
        endPtr = head
        while endPtr.next != None:
            endPtr = endPtr.next
            size += 1
        k = k % size
        if k == 0:
            return head
        secPtr = head
        i = 0
        while i < size - k - 1:
            secPtr = secPtr.next
            i += 1
        dummy = ListNode(0)
        if secPtr.next == None:
            dummy.next = head
        else:
            dummy.next = secPtr.next
        endPtr.next = head
        secPtr.next = None
        return dummy.next