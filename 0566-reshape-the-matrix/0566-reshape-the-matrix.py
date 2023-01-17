class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        if r * c != (len(mat) * len(mat[0])):
            ans = mat
        else:
            ans =[[] for i in range(r)]
            hold = [] * len(mat)
            row = len(mat)
            column = len(mat[0])
            for i in range(row):
                for j in range(column):
                    hold.append(mat[i][j])  
            index = 0
            for i in range(r):
                for j in range(c):
                    ans[i].append(hold[index])
                    index +=1
        return ans