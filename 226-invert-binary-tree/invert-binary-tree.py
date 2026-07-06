# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base case: return None when there is no more node
        if not root:
            return None
        
        # At each node, swap the left and right children.
        root.left, root.right = root.right, root.left

        #Then recursively invert the left subtree and right subtree.
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
        