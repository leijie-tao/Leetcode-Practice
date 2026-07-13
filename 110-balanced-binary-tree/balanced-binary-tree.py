# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #-------------Brute Force-------------
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        leftheight = self.getHeight(root.left)
        rightheight = self.getHeight(root.right)
        diff = abs(leftheight - rightheight)
        if diff > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def getHeight(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        l = self.getHeight(root.left)
        r = self.getHeight(root.right)
        return max(l, r) + 1

    

