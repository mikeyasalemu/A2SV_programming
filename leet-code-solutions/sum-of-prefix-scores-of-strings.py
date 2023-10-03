class TrieNode:
    def __init__(self):
        self.children = dict()
        self.val = 0

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
            node.val += 1
            
        # node.end = True
            

    def search(self,word):
        node = self.root
        res = 0
        for char in word:
          
          node = node.children[char]
          res += node.val
        

        return res 
      
   


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        
        self.trie = Trie()
        for word in words:
            self.trie.insert(word)
        
        ans =[]
        
        for word in words:
            val = self.trie.search(word)
            ans.append(val)
        
        return ans
        