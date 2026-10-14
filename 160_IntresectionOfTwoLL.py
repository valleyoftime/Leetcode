# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode | None:
        lengthA, lengthB = self.getLength(headA), self.getLength(headB)
        while lengthA > lengthB:
            if headA:
                headA = headA.next
                lengthA -= 1
        while lengthB > lengthA:
            if headB:
                headB = headB.next
                lengthB -= 1

        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next

    def getLength(self, head: ListNode | None) -> int:
        if not head:
            return 0
        return 1 + self.getLength(head.next)
