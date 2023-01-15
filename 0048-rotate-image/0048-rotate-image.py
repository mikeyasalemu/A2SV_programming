class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        matrix.reverse()
        i = 0
        for element in (zip(*matrix)):
            matrix[i] = list(element)
            i+=1