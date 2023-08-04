class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        
        size = len(quiet)
        graph = defaultdict(list)
        indegree = [0]*size
        que = deque()
        ans = [i for i in range(size)]

        for u, v in richer:
            graph[u].append(v)
            indegree[v]+=1
        
        for i in range(size):
            if indegree[i] == 0:
                que.append(i)
        
        while que:
            u = que.popleft()
            mini = quiet[u]

            for v in graph[u]:
                if mini < quiet[v]:
                    quiet[v] = mini
                    ans[v] = ans[u]
                
                indegree[v]-=1
                if indegree[v] == 0:
                    que.append(v)
        
        return ans