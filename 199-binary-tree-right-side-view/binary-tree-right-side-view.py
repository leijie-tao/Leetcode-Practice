# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # #-------------- BFS: Lst node of each layer -----------
    # def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    #     # Handle edge case
    #     if not root:
    #         return []

    #     res = []
    #     queue = deque([root])
    #     while queue:
    #         n = len(queue)
    #         # Pop n-1 nodes, and keep the last node of each layer
    #         for _ in range(n - 1):
    #             node = queue.popleft()
    #             if node.left:
    #                 queue.append(node.left)
    #             if node.right:
    #                 queue.append(node.right)
    #         core_node = queue.popleft()
    #         res.append(core_node.val)
    #         #Remeber!!!! Add the sub-nodes of core_node into queue
    #         if core_node.left:
    #              queue.append(core_node.left)
    #         if core_node.right:
    #             queue.append(core_node.right)

    #     return res



     #--------------- DFS: Right-First Traversal ------------
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(root, depth):
            if not root:
                return
            # Key part: Record the first node when we first reach this layer
            if len(res) == depth:
                res.append(root.val)
            # Recursively visit the right child first.
            dfs(root.right, depth + 1)
            dfs(root.left, depth + 1)

        dfs(root, 0)
        return res
            