class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        def dfs(row):
             # visited.add((row, col))
             for i in range(len(isConnected)):
                if i == row:
                    visited.add((row,i))
                elif (row,i) not in visited and isConnected[row][i] == 1:
                    visited.add((row,i))
                    visited.add((i,row))
                    dfs(i)
                    
        ans = 0
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if (i,j) not in visited and isConnected[i][j] == 1:
                    dfs(i)
                    ans +=1
        return ans