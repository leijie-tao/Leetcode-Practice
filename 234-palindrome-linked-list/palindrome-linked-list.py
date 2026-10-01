# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # # ------------ TC: O(N)   SC: O(N)--------------
    # def isPalindrome(self, head: ListNode | None) -> bool:
    #     nums = []
    #     cur = head
    #     while cur:
    #         nums.append(cur.val)
    #         cur = cur.next
    #     return nums == nums[::-1]



    # ------------ TC: O(N)   SC: O(1)--------------
    def isPalindrome(self, head: ListNode | None) -> bool:
        if not head or not head.next:
            return True

        # 1. Find the middle position
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. reverse the second part (start from slow to the end)
        prev = None
        cur = slow
        while cur:
            post = cur.next
            cur.next = prev
            prev = cur
            cur = post

        # 3. compare two linked list (different -> False     same -> True)
        p1 = head
        p2 = prev     
        while p2:          
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        return True