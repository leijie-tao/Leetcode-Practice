# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        # Add dummy before head to avoid the discussion of deleting head node
        prev = dummy = ListNode(next = head)
        cur = head
        while cur:
            if cur.val == val:
                post = cur.next
                prev.next = post
            else:
                prev = cur
            cur = cur.next
                
        
        return dummy.next