class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        queue = deque()
        vis = set()

        direction = [(0,1),(1,0),(-1, 0),(0, -1)]

        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] == 1:
                    row = i
                    col = j
        
        queue.append((row,col))
        vis.add((row,col))
        seque = deque([(row,col,0)])
        grid[row][col] = 2
        while queue:
            row, col = queue.popleft()

            for i , j in direction:
                    new_row = row+i
                    new_col = col + j

                    if (-1< new_row<len(grid)) and (-1< new_col<len(grid)) and grid[new_row][new_col] == 1:
                        queue.append((new_row,new_col))
                        grid[new_row][new_col] = 2
                        seque.append((new_row,new_col,0))
        ans = -1
        while seque:
            print("yeah")
            row, col, val = seque.popleft()
            
            for i , j in direction:
                    new_row = row+i
                    new_col = col + j

                    if (-1< new_row<len(grid)) and (-1< new_col<len(grid)):
                        if grid[new_row][new_col] == 0:
                            grid[new_row][new_col] = -1
                            seque.append((new_row,new_col,val+1))
                        elif grid[new_row][new_col] == 1:
                            return val
        # return 1