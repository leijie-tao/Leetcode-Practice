# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy =  ListNode(-1) #创建虚拟头节点，可直接以dummy.next为头节点，省去判断l1/l2谁是头节点
        curr = dummy
        while list1 and list2:
            if list1.val <= list2.val: 
                curr.next = list1 #谁更小，把谁接在curr后
                list1 = list1.next #同时移动到list1的下一个节点
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next   #移动curr到下一个节点
        curr.next = list1 if list1 else list2  #其中一个list走完后，直接把剩下的接在curr后
        return dummy.next
                


