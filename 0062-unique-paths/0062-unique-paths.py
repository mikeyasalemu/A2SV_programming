class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        state = [[0]* (n + 1) for _ in range(m+1)]
        state[m-1][n-1] = 1
        
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                state[i][j] += state[i+1][j] + state[i][j+1]

        return state[0][0]
        