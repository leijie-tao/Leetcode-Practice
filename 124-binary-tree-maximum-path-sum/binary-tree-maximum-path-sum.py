# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# ------------------- DFS -------------------
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = float('-inf')
        def dfs(node):
            if not node:
                return 0
            # If subtree is negative, exclude it from path sum by using 0
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)
            # max path through current node = left + right + node
            cur = left + right + node.val
            if cur > self.res:
                self.res = cur
            # return the max path sum of one subtree
            return max(left,right) + node.val

        dfs(root)
        return self.res



