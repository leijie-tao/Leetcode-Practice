class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # 1. Create a Trie
        root = TrieNode()
        for w in words: #Loop through each word
            node = root
            for char in w: #Loop through each character
                if char not in node.children:
                    node.children[char] = TrieNode() #Add the character as child node
                node = node.children[char]
            node.word = w #Record the whole word at the end of the Trie
        
        m, n = len(board), len(board[0])
        res = []

        # 2. DFS & Backtrack
        def dfs(r, c, node):
            #Start searching from the coordinate(r,c)
            char = board[r][c]
            ## If meet a new character, the path is wrong and return
            if char not in node.children:
                return
            
            ## If meet the right character, move to the child node
            next_node = node.children[char]
            ## If the child node is the last node, add the recorded word to the result, and update the last node to None to avoid adding twice 
            if next_node.word:
                res.append(next_node.word)
                next_node.word = None 
            
            # Mark the coordinate that has been visited
            board[r][c] = "#"
            
            #Continue searching for the character around the coordinate
            for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    dfs(nr, nc, next_node) #If success, continue dfs to the next node
            
            # If fail, recover the character
            board[r][c] = char

        #Pruning: delete the nodes whose child nodes are all found.
        #     if not next_node.children:
        #         del node.children[char]

        # execute dfs for each character on the graph
        for i in range(m):
            for j in range(n):
                dfs(i, j, root)
                
        return res