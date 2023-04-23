class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        direction = [(0,1),(1,0),(0,-1),(-1,0)]
        visited = set()
        def valid(i,j):
            if i < len(grid1) and i >= 0 and j< len(grid1[0]) and j >= 0:
                return True
            return False
        def dfs(row,col):
            visited.add((row,col))
            self.change.append([row,col])
            for i , j in direction:
                new_row = row + i
                new_col= col + j
                if valid(new_row,new_col) and (new_row,new_col) not in visited and grid2[new_row][new_col] == 1:
                    dfs(new_row,new_col)
        ans = 0         
        for i in range(len(grid1)):
            for j in range(len(grid1[0])):
                if (i,j) not in visited and grid2[i][j] == 1:
                    self.check = True
                    self.change = []
                    dfs(i,j)
                    for row,col in self.change:
                        if grid1[row][col] == 0:
                            self.check = False
                    if self.check:
                        ans+=1
        
        return ans