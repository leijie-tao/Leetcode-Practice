# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # #-------------Brute Force-------------
    # def isBalanced(self, root: Optional[TreeNode]) -> bool:
    #     #Base case
    #     if not root:
    #         return True
    #     #Get the height with getHeight(), and set the failure condition
    #     leftheight = self.getHeight(root.left)
    #     rightheight = self.getHeight(root.right)
    #     diff = abs(leftheight - rightheight)
    #     if diff > 1:
    #         return False
    #     #Recursion of sub-tree
    #     return self.isBalanced(root.left) and self.isBalanced(root.right)

    # def getHeight(self, root: Optional[TreeNode]) -> int:
    #     if not root:
    #         return 0
    #     l = self.getHeight(root.left)
    #     r = self.getHeight(root.right)
    #     return max(l, r) + 1



    # #-----Combine height calculation with balance judgement.  O(n^2) ——> O(n)----------
    # # To combine checking process and height calculation, use -1 to mark imbalanced.
    # def isBalanced(self, root: Optional[TreeNode]) -> bool:
    #     # Use check to return -1 for imbalanced subtree and reurn the height for balanced subtree
    #     def check(node):
    #         if not node:
    #             return 0
    #         # If the subtree is imbalanced, return -1 directly
    #         left = check(node.left)
    #         if left == -1:
    #             return -1
    #         right = check(node.right)
    #         if right == -1:
    #             return -1
    #         # If the subtree is balanced, check the difference of current layer
    #         if abs(left - right) > 1:
    #             return -1
    #         # If there is no imbalanced tree, return the current height
    #         else:
    #             return max(left, right) + 1
        
    #     return check(root) != -1


    # --------------- DFS ----------------
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [True, 0]
            # Get the result from subtrees first, and then decide what to reurn
            left, right = dfs(root.left), dfs(root.right)
            if abs(left[1] - right[1]) > 1 or left[0] == False or right[0] == False:
                return [False, -1]
            else:
                height = max(left[1], right[1]) + 1
                return [True, height]

        return dfs(root)[0]
