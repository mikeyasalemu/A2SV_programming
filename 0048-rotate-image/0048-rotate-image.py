class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
         # n by n matrix 
        side_length = len(matrix) 
        if side_length == 1 : 
            return 
        
        for row in range(side_length//2) : 
          
            col_lim = side_length - row - 1 
           
            for col in range(row, col_lim) :
               
                row_lim = side_length - col - 1
              
                matrix[row][col], matrix[col][col_lim], matrix[col_lim][row_lim], matrix[row_lim][row] = matrix[row_lim][row], matrix[row][col], matrix[col][col_lim], matrix[col_lim][row_lim]
       