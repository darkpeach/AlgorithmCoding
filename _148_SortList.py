# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        def merge(list1, list2):
            if list1 == None:
                return list2
            if list2 == None:
                return list1
            head = None
            if list1.val < list2.val:
                head = list1
                list1 = list1.next
            else:
                head = list2
                list2 = list2.next
            temp = head
            while list1 and list2:
                if list1.val < list2.val:
                    temp.next = list1
                    temp = list1
                    list1 = list1.next
                else:
                    temp.next = list2
                    temp = list2
                    list2 = list2.next

            if list1 != None:
                temp.next = list1
            if list2 != None:
                temp.next = list2

            return head

        ########################################
        if head == None or head.next == None:
            return head
        slow, fast = head, head
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None

        list1 = self.sortList(head)
        list2 = self.sortList(mid)

        sortedList = merge(list1, list2)
        return sortedList