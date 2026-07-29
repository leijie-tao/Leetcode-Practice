class TrieNode:
    def __init__(self):
        self.children = {}  # Each node stores its children 
        self.is_end = False   # Each node redords the end

class Trie:

    def __init__(self):
        self.root = TrieNode() # Create a TrieNode as root

    def insert(self, word: str) -> None:
        node = self.root    #Start from the root
        for char in word:
            # Use char as key, and use TrieNode as value
            if char not in node.children:
                node.children[char] = TrieNode() #if the key doesn't exist, create a new key and its value (trienode)
            node = node.children[char] # move to the child node
        node.is_end = True      #mark the end of a word after iterating all characters of the word

    def search(self, word: str) -> bool:
        node = self.root    #Start from the root
        for char in word:
            if char not in node.children:
                return False    #if the key isn't found, return false.
            node = node.children[char]  #otherwise, move to the next node
        return node.is_end    #check if it's the end

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)