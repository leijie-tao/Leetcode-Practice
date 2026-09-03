# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # # All paths in this tree (visit each node of the tree)
    # def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
    #     if not root:
    #         return 0
    #     # count all paths start from root + recursion in left subtree + recursion in right subtree
    #     return (self.countFrom(root, targetSum) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum))

    # # All paths start from a specific node, and count the number of paths
    # def countFrom(self, node, targetSum):
    #     if not node:
    #         return 0
    #     if node.val == targetSum:
    #         cnt = 1  
    #     else:
    #         cnt = 0
    #     cnt += self.countFrom(node.left, targetSum - node.val) 
    #     cnt += self.countFrom(node.right, targetSum - node.val)
    #     return cnt


#----------------- Refine -----------------    
# Use prefix to record the sum (root —> current), then start node is (prefix - target)
# The number of total paths <——> The number of valid (prefix - target)
    def pathSum(self, root, target):
        prefix = defaultdict(int)
        prefix[0] = 1
        self.count = 0

        def dfs(node, cur):
            if not node:
                return
            
            cur += node.val             
            self.count += prefix[cur - target]   # look up how many ancestors whose prefix = cur-target
            prefix[cur] += 1             
            dfs(node.left, cur)
            dfs(node.right, cur)
            prefix[cur] -= 1             # withdraw current layer to maintain valid prefix

        dfs(root, 0)
        return self.count