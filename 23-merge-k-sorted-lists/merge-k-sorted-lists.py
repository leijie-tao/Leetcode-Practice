# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        dummy = ListNode(-1)
        curr = dummy
        minheap = []
        # 将每个链表的头节点入堆, 存入元组 (节点值, 计数器, 节点对象)
        for i, l in enumerate(lists):
            if l:
                heapq.heappush(minheap, (l.val, i, l))
        while minheap: #只要最小堆存在，则弹出顶端最小值的头节点
            val, i, node = heapq.heappop(minheap)
            curr.next = node  
            curr = curr.next  
            # 如果该链表还有下一个节点，继续入堆
            if node.next:
                heapq.heappush(minheap, (node.next.val, i, node.next))

        return dummy.next
            

