class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:

        dic = defaultdict(set)
        for u, v in adjacentPairs:
            dic[u].add(v)
            dic[v].add(u)
        
        dic2 = defaultdict(int)
        que = deque()
        for i in dic.keys():
            dic2[i] = len(dic[i])

        ans = []
        vis = set()
        for i in dic2.keys():
            if dic2[i] == 1:
                que.append(i)
                vis.add(i)
                ans.append(i)
                break
        
        
        while que:
            val = que.popleft()
            
            for nei in dic[val]:
                dic2[nei]-=1
                if nei not in vis and dic2[nei] <= 1:
                    ans.append(nei)
                    que.append(nei)
                    vis.add(nei)
        
        return ans