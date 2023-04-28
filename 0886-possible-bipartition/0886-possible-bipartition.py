class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        dic = defaultdict(list)
        visited = set()
        
        for node1,node2 in dislikes:
            dic[node1].append(node2)
            dic[node2].append(node1)
            
        self.check = [-1] * n
        self.ans = True
        if n == 1:
            return True
        for val in dic.keys():
            if val not in visited and self.ans:
                self.dfs(val,visited,dic)
        return self.ans
    def dfs(self,node,visited,dic):
        visited.add(node)
        for val in dic[node]:
            if not self.check:
                return 
            if val in visited:
                if self.check[val - 1] == self.check[node-1]:
                    self.ans = False
                    return 
                else:
                    continue
            if val not in visited:
                self.check[val-1] = self.check[node-1]*-1
                self.dfs(val,visited,dic)
        
        
            
                        
        