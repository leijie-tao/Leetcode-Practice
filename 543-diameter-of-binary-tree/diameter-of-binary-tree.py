# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Stop condition
        if not root:
            return 0
        #How to return the diameter of current layer? 
        #1.Get the max height of each subtree to calculate the diameter
        left_height = self.maxHeight(root.left)
        right_height = self.maxHeight(root.right)
        diameter = left_height + right_height
        #2.Return the max value of current diameter, left-subtree diameter, and right-subtree diameter 
        left_diameter = self.diameterOfBinaryTree(root.left)
        right_diameter = self.diameterOfBinaryTree(root.right)
        return max(diameter, left_diameter, right_diameter)
    
    def maxHeight(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        l = self.maxHeight(root.left)
        r = self.maxHeight(root.right)
        return max(l, r) + 1