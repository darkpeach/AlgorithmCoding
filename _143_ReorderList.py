# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next:
            return
        pSlow = head.next
        pFast = head.next.next
        while pFast and pFast.next:
            pSlow = pSlow.next
            pFast = pFast.next.next
        pFast = pSlow.next
        pSlow.next = None

        pNext = pFast.next
        pFast.next = None
        while pNext:
            temp = pNext.next
            pNext.next = pFast
            pFast = pNext
            pNext = temp
        pSlow = head
        while pFast:
            pNext = pFast.next
            pFast.next = pSlow.next
            pSlow.next = pFast
            pSlow = pSlow.next.next
            pFast = pNext
        return