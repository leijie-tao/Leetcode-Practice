# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # ---------- Recursion   TC:O(H)  SC:O(H) ------------
    def deleteNode(self, root: TreeNode | None, key: int) -> TreeNode | None:
        # Base case
        if not root:
            return root

        # check the position of key
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            # lack of one child node, return the other one
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            # have two child nodes, then find the smallest one in left subtree
            cur = root.right
            while cur.left:
                cur = cur.left
            # use the smallest node to replace current node, and delete the original small node in right tree
            root.val = cur.val
            root.right = self.deleteNode(root.right, root.val)

        return root

