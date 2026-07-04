# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #Start from dummy in case we need to remove the head
        dummy = ListNode(next = head)
        slow = fast = dummy
        #Set the distance between two pointers as n
        for _ in range(n):
            fast = fast.next
        #Keep the distance and move two pointers until fast pointer reaches the end
        while fast.next:
            slow = slow.next
            fast = fast.next
        #Have slow point to slow.next.next (remove slow.next)
        slow.next = slow.next.next

        #Complete modifying and return the head
        return dummy.next