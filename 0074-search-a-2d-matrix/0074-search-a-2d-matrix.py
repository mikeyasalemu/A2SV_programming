class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        check = False
        for i in range(len(matrix)):
            if target <= matrix[i][len(matrix[0]) -1]:
                if target in set(matrix[i]):
                    check = True
            
             
        return check