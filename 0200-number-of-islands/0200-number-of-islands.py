class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()
        def inbound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))
        def dfs(row,col):
             visited.add((row, col))
             for row_change, col_change in directions:
                 new_row = row + row_change
                 new_col = col + col_change
                 if inbound(new_row, new_col) and (new_row, new_col) not in visited and grid[new_row][new_col] == "1":
                    dfs(new_row, new_col)
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visited and grid[i][j] == "1":
                    # print("yes")
                    dfs(i,j)
                    ans +=1
        return ans
                    