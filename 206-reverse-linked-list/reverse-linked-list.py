# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None #初始化pre指针，定义cur指针指向头节点
        cur = head 
        while cur:
            temp = cur.next #暂存下节点
            cur.next = pre #反转，指针指向前
            pre = cur  #更新pre和cur
            cur = temp
        return pre