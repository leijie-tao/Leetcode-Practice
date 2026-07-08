# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # # DFS: dive into the tree until reach the leaves. Each layer collect the max sub-depth and return the (max depth + 1)
        # if not root:
        #     return 0
        # left_depth = self.maxDepth(root.left)
        # right_depth = self.maxDepth(root.right)
        # return max(left_depth, right_depth) + 1


        #BFS: Add nodes of each layer into the queue ——> pop the nodes and add the sub-node into the queue
        if not root:
            return 0
        queue = deque([root])
        depth = 0

        while queue:
            n = len(queue)
            # Deal with each layer
            for _ in range(n):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth += 1

        return depth

