class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next = ListNode(3)

l2 = ListNode(1,ListNode(2, ListNode(3)))

class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        l1[].val
