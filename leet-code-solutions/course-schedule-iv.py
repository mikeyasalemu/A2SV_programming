class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        indegree = [0]*numCourses
        dic = defaultdict(list)
        for u, v in prerequisites:
            dic[u].append(v)
            indegree[v]+= 1

        que = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                que.append(i)
        
        detect = defaultdict(set)
        val = 1
        while que:
            size = len(que)
            
            for i in range(size):
                cur = que.popleft()
                
                
                for nei in dic[cur]:
                    indegree[nei]-=1
                    detect[nei].update(detect[cur])
                    detect[nei].add(cur)
                    if indegree[nei] == 0:
                        que.append(nei)
            val+=1
        
        ans = [False]*len(queries)
        ptr = 0
        for pre, cour in queries:
            if pre in detect[cour]:
                ans[ptr] = True
            ptr+=1
        
        return ans