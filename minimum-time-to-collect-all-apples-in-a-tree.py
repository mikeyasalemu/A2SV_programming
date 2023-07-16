class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        dic = defaultdict(list)

        for x, y in edges:
            dic[x].append(y)
            dic[y].append(x)
          
        def dfs(parent, val):
            count = 0

            for neighbour in dic[val]:
                if neighbour != parent:
                    count += dfs(val, neighbour)

            if count > 0:
                return count + 2 if val > 0 else count
            
            if hasApple[val] and val > 0:
                return 2
            
            return 0

        
        ans = dfs(None, 0)

        return ans