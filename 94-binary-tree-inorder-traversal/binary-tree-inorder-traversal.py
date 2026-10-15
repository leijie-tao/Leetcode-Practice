# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # # shared list & helper function
    # def inorderTraversal(self, root: TreeNode | None) -> list[int]:
    #     res = []
    #     def dfs(node):
    #         if not node:
    #             return
    #         dfs(node.left)
    #         res.append(node.val)
    #         dfs(node.right)
        
    #     dfs(root)
    #     return res

    
    # integrate return value
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []
        left = self.inorderTraversal(root.left)
        res = [root.val]
        right = self.inorderTraversal(root.right)
        return left + res + right