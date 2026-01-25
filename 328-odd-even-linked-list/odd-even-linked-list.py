# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        odd = head #记录奇数链表的head
        even = head.next 
        even_head = even #记录偶数链表的head
        while even and even.next:  #由于先奇数再偶数，所以偶数为空时说明全部遍历完成
            odd.next = odd.next.next  #奇数指向下下位，并更新          
            odd = odd.next
            even.next = even.next.next  #偶数指向下下位，并更新  
            even = even.next
        odd.next = even_head    #将偶数链表接在奇数链表后
        return head
