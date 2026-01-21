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
        if not head or not head.next:
            return
        
        fast = slow = head 
        while fast and fast.next: #当fast走完时，slow走一半，得到中点位置
            slow = slow.next
            fast = fast.next.next
        
        curr = slow.next #curr指针指向后半段的头节点
        slow.next = None #从slow走到的中点处断开
        prev = None 
        while curr:
            tmp = curr.next #记录下一个节点
            curr.next = prev #反转指针
            prev = curr #更新prev和curr
            curr = tmp
        
        first, second = head, prev #两段链表分别从head和pre开始
        while second: #由于第二段的长度<=第一段的长度
            tmp1, tmp2 = first.next, second.next #记录修改处的后一个节点
            first.next = second #重新链接指针关系
            second.next = tmp1
            first, second = tmp1, tmp2 #移动指针到后续节点，重复执行
        

        

