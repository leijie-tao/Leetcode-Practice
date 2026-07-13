# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # #--------------- brute force ------------------
    # def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    #     #If subtree is empty, return True
    #     if not subRoot:
    #         return True
    #     #If tree is empty, return False
    #     if not root:
    #         return False
    #     # Start to compare current layers of two trees
    #     if self.isSameTree(root, subRoot):
    #         return True
    #     # Return the results of subtrees. (Use OR since if contains one subtree, the final result is True)
    #     return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    # def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    #     # Both empty, return True
    #     if not p and not q:
    #         return True
    #     # One of them is empty, return False
    #     if not p or not q:
    #         return False
    #     # Both exist, compare the value of two nodes at current layer
    #     if p.val != q.val:
    #         return False
    #     # Make sure the subtrees are all same
    #     return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)



    #------------ Combine the isSameTree with isSubTree -----------------
    # Serialize the tree and use "in" to check tuple components
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:   
        # Use serialize to get a final tuple, recording each node with its subnodes 
        def serialize(node):
            # Mark the edge
            if not node:
                return "#"  
            left = serialize(node.left)
            right = serialize(node.right)
            return f"({node.val},{left},{right})"  # return the tuple, recording the current node with its subnodes
        
        #Get the tuple of tree and subtree
        root_str = serialize(root)
        sub_str = serialize(subRoot)

        #Use "in" to check subtree
        return sub_str in root_str