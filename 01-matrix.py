class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue= deque()
        visited = set()

        direction = [(0,1),(1,0),(-1, 0),(0, -1)]
        def valid(row,col):
            if row >= 0 and col >= 0 and row < len(mat) and col < len(mat[0]):
                return True
            return  False

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    queue.append((i,j))
                    visited.add((i,j))

        current = 1
        while queue:
            size = len(queue)
            for  i in range(size):
                row , col = queue.popleft()
                for i , j in direction:
                    new_row = row+i
                    new_col = col + j
                    
                    if  valid(new_row, new_col) and (new_row, new_col) not in visited:
                        mat[new_row][new_col] = current
                        queue.append((new_row,new_col))
                        visited.add((new_row,new_col))
            current +=1   
        return mat