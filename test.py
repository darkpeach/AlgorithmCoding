from _002_AddTwoNumbers import Solution
result = Solution()
class ListNode(object):
    def __init__(self, x):
        self.val = x
        # self.next = None
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)


########

#print(result.addTwoNumbers(l1,l2))
b = ListNode(5)
print(b.val)
a = b
print(a.val)
b.val = 10
print(a.val)


