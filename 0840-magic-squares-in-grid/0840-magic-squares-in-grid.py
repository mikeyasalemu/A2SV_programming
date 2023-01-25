class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        column_end =2
        row_end = 2
        row = -1
        count = 0
        if len(grid) < 3 or len(grid[0]) < 3:
            return 0
        #
        #Iterating both for the column and row using two loops
        while row_end <= len(grid) -1:
            row +=1
            column_end = 2
            column = -1
            while column_end <= len(grid[0]) - 1:
                    column +=1
                    check = True
                    lst_row =[]
                    lst_col =[]
                    for i in range(row, row_end +1):
                        dic ={}
                        num = 0
                        if check:
                            for j in range(column,column_end+1):
                                if dic.get(grid[i][j]) or grid[i][j]< 1 or grid[i][j] > 9:
                                    check = False
                                    break
                                else:
                                    dic[grid[i][j]] = 1
                                    num += grid[i][j]
                            lst_row.append(num)        
                        else:
                            break
                    if check:
                        for i in range(column, column_end+1):
                            dic ={}
                            num = 0
                            if check:
                                for j in range(row,row_end +1):
                                    if dic.get(grid[j][i]) or grid[j][i]< 1 or grid[j][i] > 9:
                                        check = False
                                        break
                                    else:
                                        dic[grid[j][i]] = 1
                                        num += grid[j][i]
                                lst_col.append(num)
                            else:
                                break
                        diagonal1 = grid[row][column] + grid[row+1][column+1] + grid[row+2][column+2]
                        diagonal2 = grid[row][column+2] + grid[row+1][column+1] + grid[row+2][column] 

                    if check:
                        for i in range(3):
                            if lst_row[i] != lst_col[i] or lst_col[i] != diagonal1 or lst_col[i] != diagonal2:
                                check = False
                        if check:
                            count +=1
                    
                    column_end += 1
            
            row_end += 1
            
        return count