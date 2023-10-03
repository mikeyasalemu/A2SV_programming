class TrieNode:
    def __init__(self):
        self.children = dict()
        self.end = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        self.dic = defaultdict(int)

    def addWord(self, word: str) -> None:
        node = self.root
        size = len(word)
        for i in range(size):
            if word[i] not in node.children:
                node.children[word[i]] = TrieNode()
                
            node = node.children[word[i]]
        node.end = True
    def search(self, word: str) -> bool:
        self.ans = False
        node = self.root
        
        def dfs(word, idx, node):
            if idx < len(word) and not self.ans:
                if word[idx] != '.' and word[idx] not in node.children:
                    return

                if word[idx] == '.':
                    for ch in node.children:
                        
                        dfs(word, idx+1, node.children[ch])
                        

                elif word[idx] in node.children:
                    dfs(word, idx+1, node.children[word[idx]])
                    
            else:
                if node.end:
                    self.ans = True
                return 
        dfs(word, 0, node)
        
        return self.ans
                


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)