# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # Key Point: intersection means `same pointer` to a node.    Not just same node value!!
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # Get length
        def getLength(head: ListNode):
            cur = head
            count = 0
            while cur:
                count += 1
                cur = cur.next
            return count

        # Align the end to make sure 2 linked lists start with same length 
        lenA = getLength(headA)
        lenB = getLength(headB)
        curA, curB = headA, headB
        if lenA >= lenB:
            diff = lenA - lenB
            for _ in range(diff):
                curA = curA.next
        else:
            diff = lenB - lenA
            for _ in range(diff):
                curB = curB.next

        # Pointers move together until find the intersection
        while curA and curB:
            if curA == curB:
                return curA
            else:
                curA = curA.next
                curB = curB.next

        return None


