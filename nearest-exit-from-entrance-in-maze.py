class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        

        direction = [(0,1),(1,0),(-1, 0),(0, -1)]

        queue = deque([(entrance[0],entrance[1],0)])
        vis = set()
        vis.add((entrance[0],entrance[1]))
        while queue:

            row, col, val = queue.popleft()

            for i , j in direction:
                    new_row = row+i
                    new_col = col + j

                    if (new_row,new_col) not in vis and (-1< new_row<len(maze)) and (-1< new_col<len(maze[0])) and maze[new_row][new_col] == '.':
                        if new_row == (len(maze)-1) or new_col == (len(maze[0])-1) or new_row == 0 or new_col == 0:
                            return val+1
                        else:
                            queue.append((new_row,new_col,val+1))
                            vis.add((new_row,new_col))
        return -1