class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        lst_row = set()
        lst_clm = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                 if matrix[i][j] == 0:
                        lst_row.add(i)   
                        lst_clm.add(j)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                 if i in lst_row or j in  lst_clm:
                        matrix[i][j] = 0 
               