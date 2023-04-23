class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        direction = [(0,1),(1,0),(0,-1),(-1,0)]
        visited = set()
        def valid(i,j):
            if i < len(board) and i >= 0 and j< len(board[0]) and j >= 0:
                return True
            return False
        def dfs(row,col):
            visited.add((row,col))
            self.change.append([row,col])
            for i , j in direction:
                new_row = row + i
                new_col= col + j
                if not valid(new_row,new_col):
                    self.check = False
                elif valid(new_row,new_col) and (new_row,new_col) not in visited and board[new_row][new_col] == "O":
                    dfs(new_row,new_col)
                    
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i,j) not in visited and board[i][j] == 'O':
                    self.check = True
                    self.change = []
                    dfs(i,j)
                    if self.check:
                        for row,col in self.change:
                            board[row][col] = 'X'
                    