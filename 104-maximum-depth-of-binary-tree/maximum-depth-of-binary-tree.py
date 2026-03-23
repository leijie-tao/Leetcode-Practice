# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #bottom-up: dfs to the bottom and return (depth+1) 
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        leftdepth = self.maxDepth(root.left)
        rightdepth = self.maxDepth(root.right)
        return 1 + max(leftdepth, rightdepth)

    # #top-down:pass depth —> helper: def dfs(node,depth) —>  update maxdepth
    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    #     maxdepth = 0
    #     if not root:
    #         return 0
    #     def dfs(node, depth):
    #         nonlocal maxdepth
    #         if not node:
    #             return 
    #         if not node.left or not node.right:
    #             maxdepth = max(maxdepth, depth)
    #         dfs(node.left, depth+1)
    #         dfs(node.right, depth+1)
    #     dfs(root, 1)
    #     return maxdepth
        
