# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    ## ------------ DFS : check a node has valid return from both sub-trees ----------------------
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         # Base case: return p/q or None
#         if not root or root == p or root == q:
#             return root

#         # Each layer: check if both left-tree and right-tree return value
#         left = self.lowestCommonAncestor(root.left, p, q)
#         right = self.lowestCommonAncestor(root.right, p, q)
#         if right and left:
#             return root

#         # Either left or right has value, return it to upper layer
#         return left or right




 #------------------- Iteration: use the nature of BST ----------------------
 # Common ancestor ——> q <= root.val <= p
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root

        while cur:
            # If both p and q are larger than cur, move cur to the right sub-tree
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            # If both p and q are smaller than cur, move cur to the left sub-tree
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            # Otherwise, curr is between p and q
            else:
                return cur
    