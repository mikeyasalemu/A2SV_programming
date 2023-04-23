class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        dic = {}
        for i in range(len(bombs)):
            dic[i] = []
        for i in range(len(bombs)):
            for j in range(len(bombs)):
                if i != j:
                    x1 = bombs[i][0]
                    y1 = bombs[i][1]
                    x2 = bombs[j][0]
                    y2 = bombs[j][1]
                    if math.sqrt(((x1 - x2)**2) + ((y1 - y2)**2)) <= bombs[i][2]:
                        dic[i].append(j)
                        
        self.count = 0
        def dfs(ind):
            visited.add(ind)
            self.count+=1
            for i in dic[ind]:
                if i not in visited:
                    dfs(i)
        ans = 0
        
        for i in dic:
            visited= set()
            self.count = 0
            dfs(i)
            ans = max(ans,self.count)
        
        return ans