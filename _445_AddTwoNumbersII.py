import math
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        pre = None
        while head:
            temp = head.next
            head.next = pre
            pre = head
            head = temp
        return pre
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = current = ListNode(0)
        carry = 0
        l1  = self.reverse(l1)
        l2  = self.reverse(l2)
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
            sum = carry % 10
            carry = int(math.floor(carry / 10))
            current.next = ListNode(sum)
            current = current.next
        result = self.reverse(dummy.next)
        return result