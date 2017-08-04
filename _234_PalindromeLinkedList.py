class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # check if the linklist is empty,
        if not head:
            return True
        fast, slow = head.next, head
        # use two pointer to find the middle point of the list
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        second = slow.next
        slow.next = None
        #reverse the second half of the list and store with in the origin list
        node = None
        while second:
            temp = second.next
            second.next = node
            node = second
            second = temp
        #campare the two half list
        while node:
            if node.val != head.val:
                return False
            node = node.next
            head = head.next
        return True
