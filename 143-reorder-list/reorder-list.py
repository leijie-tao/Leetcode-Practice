# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:   
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        mid = self.middleNode(head)         #Find the middle node
        head2 = self.reverseList(mid)       #Reverse the second part and return the new head
        while head2.next:
            #Record the next nodes of two list
            nxt = head.next
            nxt2 = head2.next
            #Reorder the list by adding the nodes in sequence
            head.next = head2
            head2.next = nxt
            #Move the pointers
            head = nxt
            head2 = nxt2

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre, cur = None, head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre