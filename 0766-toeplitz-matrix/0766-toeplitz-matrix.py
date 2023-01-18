class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        row,col = len(matrix),len(matrix[0])
        for r in range(1,row):
            for c in range(1,col):
                if matrix[r][c]!=matrix[r-1][c-1]:
                    return False
        return True