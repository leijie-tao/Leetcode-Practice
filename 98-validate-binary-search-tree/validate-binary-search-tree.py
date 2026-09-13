# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# ❌only check node.left.val < node.val < node.right.val   -----> can't promise the whole tree
# ✅ use a range (low, high) to ensure the whole tree is a BST

class Solution:
    # # ------------- DFS: use low and high -----------------
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, low, high):
            # Stop condition
            if not node:
                return True
            if not low < node.val < high:
                return False
            # Update low & high boundary
            left = dfs(node.left, low, node.val)
            right = dfs(node.right, node.val, high)
            return left and right

        return dfs(root, float('-inf'), float('inf'))
    

    ## ---------- BFS: Add each node into queue, regarding its parent as boundary -----------------
    # # node.left—> (-∞, node.val)    node.val—>(-∞, +∞)      node.right—>(node.val, +∞)
    # def isValidBST(self, root: Optional[TreeNode]) -> bool:
    #     if not root:
    #         return True
    #     # Add root and its boundary into queue
    #     queue = deque([(root, float("-inf"), float("inf"))])
    #     while queue:
    #         # Pop and check the order
    #         node, left, right = queue.popleft()
    #         if not (left < node.val < right):
    #             return False
    #         # Add the sub-nodes and their boundary into queue
    #         if node.left:
    #             queue.append((node.left, left, node.val))     #(-∞, node.val)
    #         if node.right:
    #             queue.append((node.right, node.val, right))   #(node.val, +∞)
    #     return True
