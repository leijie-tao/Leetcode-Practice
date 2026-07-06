# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# # DFS: Go through each branch (Recursion).
# class Solution:
#     def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
#         # Base case: return None when there is no more node
#         if not root:
#             return None
        
#         # At each node, swap the left and right children.
#         root.left, root.right = root.right, root.left

#         #Then recursively invert the left subtree（first) and right subtree(second).
#         self.invertTree(root.left)
#         self.invertTree(root.right)

#         return root


# BFS: Go through each layer (Queue).
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        #Create a queu, and add the [root]
        queue = deque([root])
        #while loop to deal with each layer
        while queue:
            node = queue.popleft()
            node.left, node.right = node.right, node.left
            # Add child nodes into the queue
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return root