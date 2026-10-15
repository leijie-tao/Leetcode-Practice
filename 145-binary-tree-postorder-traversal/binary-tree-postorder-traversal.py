# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # # -------- Recursion: O(n) --------
    # def postorderTraversal(self, root: TreeNode | None) -> list[int]:
    #     res = []
    #     def dfs(node):
    #         if not node:
    #             return
    #         dfs(node.left)
    #         dfs(node.right)
    #         res.append(node.val)
        
    #     dfs(root)
    #     return res


    # ---------- Iteration: O(n) ---------
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        stack = []
        cur = root
        prev = None     #marked last right node that has been visited
        res = []
        while cur or stack:
            # add all left node into stack
            while cur:
                stack.append(cur)
                cur = cur.left
            # check each left node, starting from stack top. If there is a right subtree and it's unvisited (prev hasn't moved to here), move cur to the right side.
            node = stack[-1]
            if node.right and node.right != prev:
                cur = node.right
            else:
                # after dealing with right subtree (node.right has been visited), add new stack top into res
                stack.pop()
                res.append(node.val)
                prev = node

        return res
 