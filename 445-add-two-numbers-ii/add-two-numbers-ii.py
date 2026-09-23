# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        # Reverse linked list ---> start from ones
        def reverseLinkedList(head):
            prev = None
            cur = head
            while cur:
                pos = cur.next
                cur.next = prev
                prev = cur
                cur = pos
            return prev
        l1 = reverseLinkedList(l1)
        l2 = reverseLinkedList(l2)

        # Create a new linked lsit using dummy. (dummy.next is head and move tail to update)
        dummy = ListNode()
        tail = dummy
        carry = 0       # IMPORTANT: use carry to record
        while l1 or l2 or carry:
            if l1:
                v1 = l1.val
            else:
                v1 = 0
            if l2:
                v2 = l2.val
            else:
                v2 = 0
            total = v1 + v2 + carry
            carry = total // 10
            digit = total % 10

            # add the new node and move all pointers
            tail.next = ListNode(val = digit)
            tail = tail.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return reverseLinkedList(dummy.next)


