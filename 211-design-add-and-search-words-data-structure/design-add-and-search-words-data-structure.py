class TrieNode:
    def __init__(self):
        self.children = {}
        self.isend = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isend = True

    def search(self, word: str) -> bool:
        def dfs(index, node):
            curr = node
            for i in range(index, len(word)): #Loop through the word from index
                char = word[i]
                if char == '.':    #If char is a dot, loop through all the child nodes
                    for child in curr.children.values():
                        if dfs(i + 1, child): #Recursively check the subtree of one child node
                            return True
                    return False
                else:             #If char isn't a dot, check if char is in the child nodes
                    if char not in curr.children:
                        return False
                    curr = curr.children[char]
            return curr.isend
        return dfs(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)