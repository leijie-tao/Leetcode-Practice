# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a new linked list to record the result
        dummy = ListNode(0)          
        tail = dummy                 
        carry = 0             # Use carry to record 

        # As long as there is a node of l1, l2, or carry to create a new node, keep running
        while l1 or l2 or carry:     
            if l1:
                v1 = l1.val
            else:
                v1 = 0
            
            if l2:
                v2 = l2.val
            else:
                v2 = 0
            # Calculate total value, carry value, and current digit
            total = v1 + v2 + carry  
            carry = total // 10      
            digit = total % 10       

            # Add new nodes to the end of new linked list & move all pointers
            tail.next = ListNode(digit)  
            tail = tail.next  
            if l1: 
                l1 = l1.next      
            if l2: 
                l2 = l2.next      

        return dummy.next  