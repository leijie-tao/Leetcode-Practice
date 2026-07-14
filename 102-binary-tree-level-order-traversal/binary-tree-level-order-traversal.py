# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # #---------------- BFS: Add each layer ---------------
    # def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    #     # Handle empty tree
    #     if not root:
    #         return []
    #     # Create a queue to store nodes by layer
    #     res = []
    #     queue = deque([root])
    #     while queue:
    #         n = len(queue)
    #         tmp = []
    #         # pop the nodes at current layer, and add nodes of next layer
    #         for _ in range(n):
    #             node = queue.popleft()
    #             tmp.append(node.val)
    #             if node.left:
    #                 queue.append(node.left)
    #             if node.right:
    #                 queue.append(node.right)
    #         res.append(tmp)
    #     return res


    #------------------ DFS + list[depth] ---------------
        def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
            res = []
            def dfs(node, depth):
                #Base case: return when reach leaf nodes
                if not node:
                    return
                #Each layer: add the node.val into list by depth
                if len(res) == depth:   # The first time to reach this depth
                    res.append([])
                res[depth].append(node.val)
                # Recursion: node.left & node.right
                dfs(node.left, depth + 1)
                dfs(node.right, depth + 1)

            dfs(root, 0)
            return res