class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        check = False
        for i in range(len(matrix)):
            if target in set(matrix[i]):
                check = True
            
             
        return check