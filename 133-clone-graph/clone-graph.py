"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else [] #已定义.neighbors返回邻居节点
"""

from typing import Optional
class Solution:
    # ------- Time Complexity: O(V+E)    Space Complexity: O(V) --------
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        visit = {}  #save {original_node : cloned_node}  --> avoid cycles
        def dfs(cur): #start from a node, and return the copy
            # 1️⃣if the node is cloned, return cloned node
            if cur in visit:
                return visit[cur]
            
            # 2️⃣if it's a new node, create the copy and add it to visit list
            copy = Node(cur.val)
            visit[cur] = copy

            for neighbor in cur.neighbors:
                copy.neighbors.append(dfs(neighbor))  #recursively clone all neighbors and add them to the list
            
            return copy

        return dfs(node)
        
        