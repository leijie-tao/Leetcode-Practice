# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # # ------------- DFS: Check the relationship among node.val, low and high -----------------
    # def isValidBST(self, root: Optional[TreeNode]) -> bool:
    #     def dfs(node, low, high):
    #         if not node:
    #             return True
    #         # Each layer check the range
    #         if not (low < node.val < high):
    #             return False
    #         # check the subtree with the updated boundary value
    #         return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)
        
    #     return dfs(root, float('-inf'), float('inf'))
    

    # ---------- BFS: Add each node into queue, regarding its parent as boundary -----------------
    # node.left—> (-∞, node.val)    node.val—>(-∞, +∞)      node.right—>(node.val, +∞)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        # Add root and its boundary into queue
        queue = deque([(root, float("-inf"), float("inf"))])
        while queue:
            # Pop and check the order
            node, left, right = queue.popleft()
            if not (left < node.val < right):
                return False
            # Add the sub-nodes and their boundary into queue
            if node.left:
                queue.append((node.left, left, node.val))     #(-∞, node.val)
            if node.right:
                queue.append((node.right, node.val, right))   #(node.val, +∞)
        return True
