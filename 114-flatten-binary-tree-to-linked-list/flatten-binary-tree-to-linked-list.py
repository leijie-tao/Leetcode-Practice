# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:       
    def __init__(self):
        self.last = None

    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return
        
        # 逆向操作：右 -> 左 -> 根，从右下开始向上连接
        self.flatten(root.right)
        self.flatten(root.left)
        
        #节点右子树接last，左子树设空，再更新last为当前节点
        #先把后面的排列好，再让上一层节点指向后面
        root.right = self.last
        root.left = None
        self.last = root
