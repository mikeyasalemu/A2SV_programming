class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        check = True
        for i in range(9):
            dic = {}
            for j in range(9):
                if dic.get(board[i][j]):
                    return False
                elif board[i][j] != ".":
                    dic[board[i][j]] = 1
                    
        if check:
            for i in range(9):
                dic = {}
                for j in range(9):
                    if dic.get(board[j][i]):
                        return False
                    elif board[j][i] != ".":
                        dic[board[j][i]] = 1
        if check:
            for i in range(0, 9, 3):
                for j in range(0, 9, 3):
                    dic = {}
                    for x in range(i, i+3):
                        for y in range(j, j+3):
                                if dic.get(board[x][y]):
                                    return False
                                elif board[x][y] != ".":
                                    dic[board[x][y]] = 1
                
        return check
        
       
        