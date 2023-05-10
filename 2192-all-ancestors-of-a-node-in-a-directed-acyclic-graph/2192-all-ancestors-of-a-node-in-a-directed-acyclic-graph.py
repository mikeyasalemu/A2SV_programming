class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        dic = defaultdict(list)
        indegree = [0]*n
        
        for num1, num2 in edges:
            dic[num1].append(num2)
            indegree[num2] += 1
        
        que = deque()
        
        for i in range(n):
            if indegree[i] == 0:
                que.append(i)
        
        ans = [set() for i in range(n)]
        
        while que:
            temp = que.popleft()
            
            for val in dic[temp]:
                ans[val].add(temp)
                ans[val].update(ans[temp])
                indegree[val] -= 1
                if indegree[val] == 0:
                    que.append(val)
        for i in range(n):
            ans[i] = (sorted(list(ans[i])))
        return ans
                