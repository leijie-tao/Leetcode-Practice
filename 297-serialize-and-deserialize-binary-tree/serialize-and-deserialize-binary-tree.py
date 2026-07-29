# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# # ---------------------- BFS ------------------------
# class Codec:
#     def serialize(self, root):
#         """Encodes a tree to a single string.
        
#         :type root: TreeNode
#         :rtype: str
#         """
#         if not root:
#             return "N"
#         res = []
#         queue = deque([root])
#         while queue:
#             node = queue.popleft()
#             if not node:
#                 res.append("N")
#             else:
#                 res.append(str(node.val))
#                 queue.append(node.left)
#                 queue.append(node.right)
#         return ",".join(res)


#     def deserialize(self, data):
#         """Decodes your encoded data to tree.
        
#         :type data: str
#         :rtype: TreeNode
#         """
#         if not data:
#             return None
#         vals = data.split(",")
#         if vals[0] == "N":
#             return None
#         root = TreeNode(int(vals[0]))   # Root is vals[0]
#         queue = deque([root])
#         i = 1                           #child nodes start from i=1
#         while queue:
#             node = queue.popleft()
#             # Buid left subnode of current node, and add the subnode into queue
#             if vals[i] != "N":
#                 node.left = TreeNode(int(vals[i]))
#                 queue.append(node.left)
#             i += 1
#             # Buid right subnode of current node, and add the subnode into queue
#             if vals[i] != "N":
#                 node.right = TreeNode(int(vals[i]))
#                 queue.append(node.right)
#             i += 1
#     return root


# --------------------- DFS (pre-order: make sure start from root)----------------------
class Codec:
    def serialize(self, root):
        res = []
        def dfs(node):
            if not node:
                res.append("N")      
                return
            # pre-order: node —> node.left —> node.right
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(res) 

    def deserialize(self, data):
        vals = data.split(",")
        # Share the index to read the string
        self.i = 0  
        def dfs():
            if vals[self.i] == "N":
                self.i += 1              
                return None
            # Build node with vals[self.i]
            node = TreeNode(int(vals[self.i]))
            self.i += 1  
            # Build all left subtrees until meet "N"                
            node.left = dfs()
            # Build all right subtrees until meet "N"                 
            node.right = dfs()           
            return node
        return dfs()   
        


        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))