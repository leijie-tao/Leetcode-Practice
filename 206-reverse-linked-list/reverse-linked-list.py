# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Key point: don't lose the rest part when reverse the linked list 
        pre = None          #After reversing, head will become the last node and point to None, which is pre.
        cur = head          #Start from head
        while cur:              
            nxt = cur.next  #Save the next node first.
            cur.next = pre  #Reverse
            pre = cur       #Update pre and cur
            cur = nxt
        return pre          #After reversing, pre will be the head