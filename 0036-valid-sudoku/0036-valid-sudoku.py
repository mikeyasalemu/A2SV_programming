class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Column check
        for i in range(9):
            dic_column = {}
            for j in range(9):
                if dic_column.get(board[i][j]):
                    return False
                elif board[i][j] != ".":
                    dic_column[board[i][j]] = 1
        #row check      
        for i in range(9):
            dic_row = {}
            for j in range(9):
                if dic_row.get(board[j][i]):
                    return False
                elif board[j][i] != ".":
                    dic_row[board[j][i]] = 1
        
        #box check
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                dic_box = {}
                for x in range(i, i+3):
                    for y in range(j, j+3):
                            if dic_box.get(board[x][y]):
                                return False
                            elif board[x][y] != ".":
                                dic_box[board[x][y]] = 1
                
        return True
        
       
        