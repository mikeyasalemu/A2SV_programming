class TrieNode:
    def __init__(self):
        self.children = dict()
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        size = len(word)
        for i in range(size):
            if word[i] not in node.children:
                node.children[word[i]] = TrieNode()
                
            
            node = node.children[word[i]]
        node.end = True
            
        # node.end = True
            

    def search(self,word):
        node = self.root
        res = 0
        for char in word:
          
          node = node.children[char]
            
          if node.end:
            res+=1
        

        return word if len(word) == res else ""


class Solution:
    def longestWord(self, words: List[str]) -> str:
        
        self.trie = Trie()
        for word in words:
            self.trie.insert(word)
        
        ans = ""
        
        for word in words:
            val = self.trie.search(word)
            if (not ans or len(ans) < len(val)) or (len(ans) == len(val) and val < ans):
                ans = val
        
        return ans
        