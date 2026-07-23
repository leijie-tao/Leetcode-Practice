# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# #------------------------ Recursive DFS ------------------------
# # In a BST, the inorder traversal (Left → Node → Right) naturally visits nodes in sorted order.
# class Solution:
#     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
#         self.k = k
#         self.res = 0

#         def dfs(node):
#             if not node:
#                 return None
#             # Left recursion
#             dfs(node.left)
#             # Node layer
#             if self.res != 0:
#                 return
#             if self.k == 1:
#                 self.res = node.val
#                 return
#             self.k -= 1
#             # Right recursion
#             dfs(node.right)

#         dfs(root)
#         return self.res
       


    # ---------------------- Iterative DFS ------------------------
    # recursion ——> this traversal with a stack ——> only visit nodes until we reach the k-th smallest. No need to traverse the whole tree.
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root

        while stack or curr:
            # Add all left nodes into the stack at first & add right nodes when move curr
            while curr:
                stack.append(curr)
                curr = curr.left
            # Start to pop from the smallest one 
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            # Move to right subtree (prepare to add node into stack & pop)
            curr = curr.right



