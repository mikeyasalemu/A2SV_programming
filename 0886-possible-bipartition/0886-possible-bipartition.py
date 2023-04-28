class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        self.dic = defaultdict(list)
        self.visited = set()
        
        for node1,node2 in dislikes:
            self.dic[node1].append(node2)
            self.dic[node2].append(node1)
        self.values = self.dic.values()
        self.check = [-1] * n
        self.ans = True
        if n == 1:
            return True
        for val in self.dic.keys():
            if val not in self.visited:
                self.dfs(val)
        return self.ans
    def dfs(self,node):
        self.visited.add(node)
        for val in self.dic[node]:
            if not self.check:
                return 
            if val in self.visited:
                if self.check[val - 1] == self.check[node-1]:
                    self.ans = False
                    return 
                else:
                    continue
            if val not in self.visited:
                self.check[val-1] = self.check[node-1]*-1
                self.dfs(val)
        
        
            
                        
        