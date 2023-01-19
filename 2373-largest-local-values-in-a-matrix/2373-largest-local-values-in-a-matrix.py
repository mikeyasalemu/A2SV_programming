class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        maxLocal = [[0]*(n-2) for _ in range(n-2)]
        for i in range(1, n-1):
            for j in range(1, n-1):
                
                lst= [[0]* 3 for _ in range(3)]
                for index1 in range(-1, 2):
                    for index2 in range(-1, 2):
                        
                        lst[index1+1][index2+1] = grid[i + index1][j + index2]
                
                maxLocal[i-1][j-1] = max(lst[0] + lst[1] + lst[2])
               
        return maxLocal
        