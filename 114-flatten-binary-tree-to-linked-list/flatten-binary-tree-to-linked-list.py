# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        
        nodes = [] #先序遍历存储节点
        def dfs(node):  
            if not node:
                return
            nodes.append(node)     
            dfs(node.left)     
            dfs(node.right)
        dfs(root)

        for i in range(len(nodes)-1): #再遍历列表按顺序连接节点（空置左树，全部移至右树）
            curr = nodes[i]
            nxt = nodes[i+1]
            curr.left = None
            curr.right = nxt
        nodes[-1].left = None
        nodes[-1].right = None
