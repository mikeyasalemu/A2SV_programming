from typing import List
from collections import defaultdict
from collections import deque
def parallelCourses(n, prerequisites):
    # Write your code here.
        indegree = [0]*n
        dic = defaultdict(list)
        for u, v in prerequisites:
            dic[u].append(v)
            indegree[v-1]+= 1
   
        que = deque()
        for i in range(n):
            if indegree[i] == 0:
                que.append(i+1)

        # ans = [0]*n
        check = 0
        val = 1
        while que:
            size = len(que)
            check+=size
            for i in range(size):
                cur = que.popleft()
                
                # ans[cur-1] = val
                for nei in dic[cur]:
                    indegree[nei-1]-=1
                    if indegree[nei-1] == 0:
                        que.append(nei)
            val+=1
            
        if check != n:
             return -1

        return val-1

        pass
