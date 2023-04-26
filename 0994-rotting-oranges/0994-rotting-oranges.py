class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        self.visited = set()
        queue = []
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i,j))
                    self.visited.add((i,j))
        direction = [(0,1),(1,0),(-1,0),(0,-1)]
        
        def valid (row,col):
            if row >= 0 and col >= 0 and row < len(grid) and col < len(grid[0]):
                return True
            return False
        self.ans = 0
        
        def bfs(current):
            
            
            temp = []
            for row,col in current:
                for i , j in direction:
                    new_row = row + i
                    new_col = col + j
                    if valid(new_row, new_col) and (new_row, new_col) not in self.visited and grid[new_row][new_col] == 1:
                        temp.append((new_row, new_col))
                        self.visited.add((new_row, new_col))
            if temp:
                bfs(temp)
                self.ans+=1
                
        bfs(queue)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in self.visited and grid[i][j] == 1:
                    return -1
        return self.ans