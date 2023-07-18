class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        dic = defaultdict(list)
        
        for i in range(1, len(parent)):
            dic[parent[i]].append(i)
        # print(dic)
        ans = 0 
        
        def dfs(node):
            nonlocal ans
			
            fir,sec = 0,0  
            
            for nei in dic[node]:
                st = dfs(nei)
                if s[nei] != s[node]:
                    if st > fir: 
                        sec = fir
                        fir = st
                    elif st == fir or st > sec: 
                        sec = st
                            
            ans = max(ans, fir+sec+1)
            return fir+1
        
        dfs(0)
        
        return ans