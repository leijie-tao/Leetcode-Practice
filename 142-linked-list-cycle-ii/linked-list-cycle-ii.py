# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        has_circle = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                has_circle = True
                break #记录相遇的位置
        if not has_circle:
            return None

        #慢指针重新回到头节点出发
        slow = head
        while slow != fast: #两指针以相同的速度前进，直到相遇
            slow = slow.next
            fast = fast.next
        return slow


#设：从起点到环入口的距离为 a。
# 从环入口到相遇点的距离为 b。
# 从相遇点再走回到环入口的距离为 c。
# 当快慢指针相遇时：
# 慢指针走的距离：L slow=a+b
# 快指针走的距离：Lfast=a+n(b+c)+b （n 是快指针在环里绕的圈数）
# 因为快指针速度是慢指针的 2 倍： 2(a+b)=a+n(b+c)+b 化简后得到： a+b=n(b+c) a=(n−1)(b+c)+c
#从起点到入口的距离 a，等于从相遇点继续往前走 c 距离，再加上若干圈环的长度。它们一定会在入口处碰头。