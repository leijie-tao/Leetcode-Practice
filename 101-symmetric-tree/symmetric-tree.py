# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        if not root:
            return True
        # Each layer checks if it's a mirror
        return self.isMirror(root.left, root.right)
    

    def isMirror(self, p:TreeNode, q: TreeNode):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        # Compare two subtrees
        return self.isMirror(p.left, q.right) and self.isMirror(p.right, q.left)