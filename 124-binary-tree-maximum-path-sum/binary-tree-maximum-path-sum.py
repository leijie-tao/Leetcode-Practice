# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# # ------------------- DFS(Intuition)-------------------
# # Every node returns a non-negative number: node.val + leftDown + rightDown
# class Solution:
#     def maxPathSum(self, root: Optional[TreeNode]) -> int:
#         res = -float('inf')
#         def dfs(node):
#             nonlocal res
#             if not node:
#                 return None
#             # Maximum downward path from left/right subtrees
#             left = self.getMax(node.left)
#             right = self.getMax(node.right)
#             # Best full path through this node
#             res = max(res, left + right + node.val)
#             # Try best full path for every node using DFS
#             dfs(node.left)
#             dfs(node.right)
#         dfs(root)
#         return res
            
        
#     def getMax(self, node):
#         if not node:
#             return 0
#         leftmax = self.getMax(node.left)
#         rightmax = self.getMax(node.right)
#         current_path = max(leftmax, rightmax) + node.val
#         #Return the current path sum, and void negative number (negative paths should be ignored)
#         return max(current_path, 0)   




# ------------------- DFS(Optimal)-------------------
# Visit each node only once.
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = -float('inf')
        def getMax(node):
            nonlocal res
            if not node:
                return 0                      
            leftmax = getMax(node.left)       
            rightmax = getMax(node.right) 
            #Update the global maximum using the "path through this node".
            res = max(res, leftmax + rightmax + node.val)
            #Return the best downward path to the parent. (Max Downward Path) (Ignore negative numbers)
            current_path = max(leftmax, rightmax) + node.val
            return max(current_path, 0)  
        getMax(root)
        return res