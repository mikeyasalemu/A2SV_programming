class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        column = len(mat[0])
        row = len(mat)
        size = column * row
        r= 0
        c = 0
        up = True
        ans  =[]
        check = 0
        while check < size:
            if up:
                ans.append(mat[r][c]) 
                temp1 = c + 1
                temp2 = r - 1
                if temp1== column  or temp2 == -1:
                    if c+1 < column:
                        c += 1
                    else:
                        r += 1
                    up = False
                else:
                    c+=1 
                    r-=1 
            else:
                ans.append(mat[r][c])
                temp1 = c - 1
                temp2 = r + 1
                if temp1 == -1  or temp2 == row:
                    if r+1 < row:
                        r += 1
                    else:
                        c += 1
                    up = True
                else:
                    c-= 1
                    r+=1
            check += 1   
        return ans