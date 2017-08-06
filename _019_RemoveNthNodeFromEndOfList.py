class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return []
        dummy = ListNode(0)
        firstPtr = head
        dummy.next = head
        preNode = dummy
        for i in range(n):
            if not firstPtr:
                return None
            firstPtr = firstPtr.next
        while firstPtr:
            firstPtr = firstPtr.next
            preNode = preNode.next
        temp = preNode.next.next
        preNode.next = temp
        return dummy.next