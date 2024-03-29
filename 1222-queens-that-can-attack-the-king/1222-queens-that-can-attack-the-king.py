class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
#         put all the possible ways the king can be captured in array
        check = [[-1, 0], [1, 0], [0,-1], [0, 1], [-1, 1], [-1, -1] ,[1, 1], [1, -1]]
        ans = []
        
#       typecast for checking in constant time
        queens = set(map(tuple, queens))
        
        for row, column in check:
            kingi = king[0]+row
            kingj = king[1]+column
            
            while 0<=kingi<8 and 0<=kingj <8:
             
                if (kingi, kingj) in queens:
                    ans.append([kingi, kingj])
                    break
                kingi+= row
                kingj+= column
            
        return ans