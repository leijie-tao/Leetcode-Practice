"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else [] #已定义.neighbors返回邻居节点
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        visited = {node: Node(node.val)}#建立以原节点为key，以克隆节点为value的访问表
        queue = deque([node]) #双端队列，任意节点作为起始入队

        while queue:
            curr = queue.popleft() #弹出当前节点
            for neighbor in curr.neighbors: #找邻居：遍历当前节点的邻居节点
                if neighbor not in visited: 
                    visited[neighbor] = Node(neighbor.val) #克隆邻居：若邻居节点未被访问过，先存至哈希表并创建克隆邻居，{哈希[原节点]:Node(克隆节点按名字生成的新地址)}
                    queue.append(neighbor) #把邻居节点入队，等待下一轮搜查
                visited[curr].neighbors.append(visited[neighbor])#与邻居建立关系：把邻居节点添加至 当前节点的邻居列表中
        
        return visited[node] #返回原节点的值，即克隆节点