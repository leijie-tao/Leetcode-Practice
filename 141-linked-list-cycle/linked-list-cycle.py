# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:   #空链表或只有一个节点，则return false
            return False

        fast = slow = head      #快慢指针同时从头出发，快指针每次2步，慢指针每次1步，相遇则说明循环
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False