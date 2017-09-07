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
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        ptr = head
        parent = dummy
        preCount = 1
        while head and head.next:
            if head.next.val != head.val:
                preCount = 1
                ptr.next = head.next
                ptr = head.next
                if parent != ptr and ptr != parent.next:
                    parent = parent.next
            else:
                if preCount == 1:
                    ptr = parent
                preCount += 1
            head = head.next
        if ptr.next:
            ptr.next = None
        return dummy.next