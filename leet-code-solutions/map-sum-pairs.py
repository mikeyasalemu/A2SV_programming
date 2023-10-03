class TrieNode:
    def __init__(self):
        self.children = dict()
        self.val = 0
        
class MapSum:

    def __init__(self):
        self.root = TrieNode()
        self.dic = defaultdict(int)
        
    def insert(self, key: str, val: int) -> None:
        red = 0
        
        if key in self.dic:
            red = self.dic[key]
            
        node = self.root
        size = len(key)
        for i in range(size):
            if key[i] not in node.children:
                node.children[key[i]] = TrieNode()
                
            
            node = node.children[key[i]]
            node.val += val - red
        """."""
        res =  node.val
        
        self.dic[key] = val


    def sum(self, prefix: str) -> int:
        node = self.root
        res = 0
        for char in prefix:
          if char not in node.children:
            
            return 0
        
          node = node.children[char]

        return node.val 


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)