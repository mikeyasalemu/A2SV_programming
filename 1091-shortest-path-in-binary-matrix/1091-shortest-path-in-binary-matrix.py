class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        queue = deque()
        visited = set()
        if grid[0][0] == 1 or grid[len(grid) -1][len(grid) -1] == 1:
            return -1
        if grid[0][0] == 0 and len(grid) == 1:
            return 1
        visited.add((0,0))
        queue.append((0,0,1))
        
        def valid(row,col):
            if row >= 0 and col >= 0 and row < len(grid) and col < len(grid[0]):
                return True
            return  False
        direction = [(0,1),(1,0),(-1, 0),(0, -1),(-1, 1),(1,-1),(1,1),(-1,-1)]
        ans = 0
        check = False
        
        while queue:
            row,col,val = queue.popleft()

            for i , j in direction:
                new_row = row+i
                new_col = col + j
                
                if valid(new_row, new_col) and (new_row, new_col) not in visited and grid[new_row][new_col] == 0:
                    
                    if (new_row, new_col) == (len(grid) -1,len(grid) -1):
                        check = True
                        ans = val+1
                        break
                    queue.append((new_row, new_col,val+1))
                    visited.add((new_row, new_col))
            
            if check:
                break
            
        if check:
            return ans
        return -1
