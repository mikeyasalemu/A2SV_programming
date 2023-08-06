from typing import List
from collections import defaultdict
from collections import deque
class Solution:
    def minimumTime(self, n : int,m : int, edges : List[List[int]]) -> int:
        # code here
        indegree = [0]*n
        dic = defaultdict(list)
        for u, v in edges:
            dic[u].append(v)
            indegree[v-1]+= 1
        
        
        
        
        que = deque()
        for i in range(n):
            if indegree[i] == 0:
                que.append(i+1)
                
        ans = [0]*n
        val = 1
        while que:
            size = len(que)
            
            for i in range(size):
                cur = que.popleft()
                
                ans[cur-1] = val
                for nei in dic[cur]:
                    indegree[nei-1]-=1
                    if indegree[nei-1] == 0:
                        que.append(nei)
            val+=1
            
        return ans


#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()



class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        a=IntArray().Input(2)
        
        
        edges=IntMatrix().Input(a[1], a[1])
        
        obj = Solution()
        res = obj.minimumTime(a[0],a[1], edges)
        
        IntArray().Print(res)
        

# } Driver Code Ends