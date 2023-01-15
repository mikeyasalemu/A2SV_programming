class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
         # n by n matrix 
        side_length = len(matrix) 
        # can be singular matrix by constraints
        if side_length == 1 : 
            return 
        # otherwise, we need to do rotations 
        # loop over half of the side sets, as rotations will accomodate other half automatically. 
        for row in range(int(side_length/2)) : 
            # column limit of rotation
            col_lim = side_length - row - 1 
            # loop columns in range 
            for col in range(row, col_lim) :
                # row limit currently  
                row_lim = side_length - col - 1
                # swap four positions each time  
                matrix[row][col], matrix[col][col_lim], matrix[col_lim][row_lim], matrix[row_lim][row] = matrix[row_lim][row], matrix[row][col], matrix[col][col_lim], matrix[col_lim][row_lim]
       