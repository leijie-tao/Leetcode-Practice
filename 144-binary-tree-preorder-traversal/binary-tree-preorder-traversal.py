# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # solution1: merge return value
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []
        res = [root.val]
        left = self.preorderTraversal(root.left)
        right = self.preorderTraversal(root.right)
        return res + left + right


    # # solution2: shared list & call helper function
    # def preorderTraversal(self, root):
    #     res = []                            
    #     def dfs(node):                        
    #         if not node:
    #             return
    #         res.append(node.val)              
    #         dfs(node.left)                     
    #         dfs(node.right)                    
    #     dfs(root)
    #     return res