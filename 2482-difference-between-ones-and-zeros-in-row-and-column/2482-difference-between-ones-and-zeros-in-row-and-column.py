import numpy as np
class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]: 
        m = len(grid)
        n = len(grid[0])
        count_row = np.zeros(m, int)
        count_clmn = np.zeros(n, int)
        
        for row in range(m):
            for clmn in range(n):
                count_row[row] += grid[row][clmn]
            
        for clmn in range(n):
            for row in range(m):
                count_clmn[clmn] += grid[row][clmn]
            
       
        for row in range(m):
            for clmn in range(n):
                grid[row][clmn] = count_row[row] + count_clmn[clmn] - (m - count_row[row]) - (n - count_clmn[clmn])
               
        return grid
        