# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)             # Use dummy node to create a new linked list
        tail = dummy                    # Similar with nxt pointer
    
        while list1 and list2:          # If two lists exist, compare the value and add the list to the end of new list.
            if list1.val <= list2.val:
                tail.next = list1
                tail = tail.next        # Move the tail and next node of list
                list1 = list1.next 
            else:
                tail.next = list2
                tail = tail.next
                list2 = list2.next 
        
        # If there is still a list, add it to the end.
        if list1:
            tail.next = list1
        else:
            tail.next = list2
        
        return dummy.next           #dummy.next is the head


    