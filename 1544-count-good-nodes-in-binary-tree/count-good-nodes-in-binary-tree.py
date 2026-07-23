# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# # ---------------------- DFS: from root to leaves ---------------------
# # The current node’s value ≥ maximum → it is a good node
# class Solution:
#     def goodNodes(self, root: TreeNode) -> int:
#         self.count = 0
#         def dfs(node, maxVal):
#             if not node:
#                 return 0
#             #Check current node first, then have recursion (left+right)
#             if node.val >= maxVal:
#                 self.count += 1
#             maxVal = max(maxVal, node.val)
#             dfs(node.left, maxVal)
#             dfs(node.right, maxVal)
#         # maxVal starts from root
#         dfs(root, root.val)
#         return self.count


# -------------------- BFS -----------------------
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        queue = deque()
        # bind node with current maxVal, and add them into queue
        queue.append((root,root.val))
        while queue:
            # Pop node and maxVal, check the node, and update maxVal
            node, maxVal = queue.popleft()
            if node.val >= maxVal:
                res += 1
                maxVal = max(maxVal, node.val)
            # Add node.left & node.right
            if node.left:
                queue.append((node.left, maxVal))
            if node.right:
                queue.append((node.right, maxVal))
        
        return res




