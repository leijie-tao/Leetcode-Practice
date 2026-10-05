# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # # ------- TC: O(n log n)   SC: O(n)------------
    # def sortList(self, head: ListNode | None) -> ListNode | None:
    #     nums = []
    #     cur = head
    #     while cur:
    #         nums.append(cur.val)
    #         cur = cur.next
    #     nums.sort()

    #     cur = head
    #     for num in nums:
    #         cur.val = num
    #         cur = cur.next
    #     return head


    def sortList(self, head: ListNode | None) -> ListNode | None:
        # Base case: no node or only one node -> in order
        if not head or not head.next:
            return head
        
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Cut linked list into two halves
        mid = slow.next
        slow.next = None

        # Recursively sort both halves.
        left = self.sortList(head)
        right = self.sortList(mid)

        # Return the merged list.
        return self.merge(left, right)


    def merge(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        dummy = ListNode()
        cur = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next


