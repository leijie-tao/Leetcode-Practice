# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# ------------------- DFS: TC:O(n)   SC:O(h)-------------------
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = float('-inf')
        def dfs(node):
            if not node:
                return 0
            # get positive value from subtree or 0
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)
            path_sum = node.val + left + right
            self.res = max(self.res, path_sum)
            # choose the subtree with larger value
            return max(left, right) + node.val
        
        dfs(root)
        return self.res
        
        
        
        
        
        
        

