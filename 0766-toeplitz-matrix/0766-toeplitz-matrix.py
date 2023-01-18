class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
          dic = {}
          check = True
          # row = len(matrix)
          # column = len(matrix[0])
          for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][j] = 100
                    
                if dic.get(i -j):
                    if dic.get(i -j) != matrix[i][j]:
                        check = False
                        break
                else:
                    dic[i-j] = matrix[i][j]
            if not check:
                break
          return check
            