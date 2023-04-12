class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()
        def inbound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))
        
        def dfs(row, col):
             if not inbound(row, col) or grid[row][col] == 0:
                    return 0
            
             visited.add((row, col))
             count = 0
             for row_change, col_change in directions:
                 new_row = row + row_change
                 new_col = col + col_change
                 if (new_row, new_col) not in visited and inbound(row, col) and grid[row][col] == 1:
                    
                    count+=dfs(new_row, new_col)
             return count+1
            
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i,j) not in visited:
                    # print("yes", dfs(i,j),i,j)
                    ans = max(dfs(i,j) , ans)
        return ans