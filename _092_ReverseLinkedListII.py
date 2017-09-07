# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        if m == 1:
            preM = dummy
        else:
            preM = self.findKth(head, m - 1)
        mthNode = preM.next
        nthNode = self.findKth(head, n)
        nNext = nthNode.next
        nthNode.next = None
        newMth = self.reverse(mthNode)
        preM.next = newMth
        mthNode.next = nNext
        return dummy.next

    def findKth(self, head, m):
        i = 1
        while i < m:
            head = head.next
            i += 1
        return head

    def reverse(self, head):
        curt = None
        while head:
            temp = head.next
            head.next = curt
            curt = head
            head = temp
        return curt

