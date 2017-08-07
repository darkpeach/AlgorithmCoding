# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# class Solution(object):
#     def swapPairs(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#         dummy = ListNode(0)
#         dummy.next = head
#         ptr = dummy.next
#         pre = dummy
#         flag = -1
#         while ptr:
#             if flag == -1:
#                 swap = ptr
#                 ptr = ptr.next
#             elif flag == 1:
#                 temp = ptr.next
#                 pre.next = ptr
#                 ptr.next = swap
#                 swap.next = temp
#                 pre = swap
#                 ptr = swap.next
#             flag = flag * -1
#         return dummy.next


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        head = dummy
        while head.next and head.next.next:
            n1 = head.next
            n2 = n1.next
            temp = n2.next
            head.next = n2
            n2.next = n1
            n1.next = temp
            head = n1
        return dummy.next

