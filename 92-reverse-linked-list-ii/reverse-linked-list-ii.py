# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        dummy = ListNode(next = head)
        prev = dummy
        # Get the linked list before reversed linked list.(left part)
        for _ in range(left - 1):
            prev = prev.next

        # Record the start of reversed linked list. And reverse the linked list.
        start = prev.next
        cur = start
        prev_in_seg = None
        for _ in range(right - left + 1):
            post = cur.next
            cur.next = prev_in_seg
            prev_in_seg = cur
            cur = post
        
        # Left part point to the new head of reversed linked list.
        prev.next = prev_in_seg
        # Let start (new tail) point to the rest part.
        start.next = cur

        return dummy.next


  
