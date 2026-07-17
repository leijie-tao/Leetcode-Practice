# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # ------------ DFS : check a node has valid return from both sub-trees ----------------------
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Base case: return p/q or None
        if not root or root == p or root == q:
            return root

        # Each layer: check if both left-tree and right-tree return value
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if right and left:
            return root

        # Either left or right has value, return it to upper layer
        return left or right




 