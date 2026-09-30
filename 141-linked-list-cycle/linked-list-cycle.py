# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Use two pointers to decide if it's a cycle
        fast = slow = head

        # check `fast` and `fast.next` are valid -> make sure we can use `fast.next.next`   
        while fast and fast.next:
            #If there is a cycle, two pointers will meet each other.
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
        
        
        
        
        
        
        
        
        
