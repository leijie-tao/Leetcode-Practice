# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# # #------------------------ DFS inorder traversal ------------------------
class Solution:
#     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
#         arr = []
#         def dfs(node):
#             if not node:
#                 return
#             dfs(node.left)
#             arr.append(node.val)
#             dfs(node.right)

#         dfs(root)
#         return arr[k - 1]


# # #------------------------ recursive DFS (call itself) ------------------------
#     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
#         self.res = None
#         self.count = 0
#         def dfs(node):
#             if not node or self.res is not None:
#                 return
#             dfs(node.left)
#             self.count += 1
#             if self.count == k:
#                 self.res = node.val
#                 return
#             dfs(node.right)

#         dfs(root)
        # return self.res



# #--------------- iterative DFS (use stack instead of recursion to simulate inorder traversal) ---------------------
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        node = root
        while stack or node:
            # Add all left nodes into stack first
            while node:
                stack.append(node)
                node = node.left
            # Simulate inorder traversal (left - root - check right)
            node = stack.pop()
            k -= 1
            if k == 0:
                return node.val
            node = node.right

