class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        self.ans = 0
        def inbound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))
        def dfs(grid, visited, row, col):
             # base case
             # nonlocal ans
             if not inbound(row, col) or grid[row][col] == 0:
                    self.ans+=1
                    return
            
             if visited[row][col]:
                return
            
             visited[row][col] = True
             for row_change, col_change in directions:
                 new_row = row + row_change
                 new_col = col + col_change
                 dfs(grid, visited, new_row, new_col)
                 # print(ans)
            
             
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    dfs(grid,visited,i,j)
                    return self.ans