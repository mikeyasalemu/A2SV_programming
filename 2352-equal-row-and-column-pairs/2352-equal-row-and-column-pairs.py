from collections import defaultdict
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = 0
        dic = defaultdict(int)
        
#         the Zip place reverses the matrix , meaning the rows to columns and vice versa
#         then add it to dictionary and increase the value byone if there is another one
        for row in zip(*grid):
            dic[row] +=1
        
#       if there is a column that is equal to that row get its value from the dictionary
        for row in grid:
            count+= dic[tuple(row)]
                    
        return count
        