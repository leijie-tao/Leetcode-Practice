# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Base case: if either array is empty, return null
        if not preorder or not inorder:
            return None
        # Use self.buildTree(preorder, inorder) to recursively build subtrees
        root = TreeNode(preorder[0]) #First element of preorder is always root
        mid = inorder.index(preorder[0]) #The index of root in inorder is mid ————> reflects the number of nodes in the left subtree
        # Left subtree: update the preorder[1, 1+node numbers] and inorder[all nodes before the root]
        # Right subtree: update the preorder & inorder range
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])
        return root
