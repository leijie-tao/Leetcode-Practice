"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None
        #创建哈希表存储克隆对象,每个指针位置对应一个节点
        mapping = {}
        curr = head
        while curr:
            mapping[curr] = Node(curr.val)
            curr = curr.next
        
        #curr从头开始，mapping[curr].next克隆节点的下一个是mapping中对应curr.next的值
        #同理，复制random连接
        curr = head
        while curr:
            mapping[curr].next = mapping.get(curr.next)
            mapping[curr].random = mapping.get(curr.random)
            curr = curr.next

        return mapping[head]