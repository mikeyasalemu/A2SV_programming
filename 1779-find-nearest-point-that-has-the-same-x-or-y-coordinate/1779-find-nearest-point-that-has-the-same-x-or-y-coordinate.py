class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        
#         assigning  result to highest value to compa the minimum value
#         and the returned value to -1 so that it will return  if it doesn't enter if stmnt
         result  = float(inf)
         hold = result
         ret = -1
         for iterator,row in enumerate(points):
             
                if row[0] == x or row[1] == y:
                    distance = abs( row[0] - x)  + abs(y-row[1])
                    result = min(distance , result)
                    
#                     cheking if the result have been changed
                    if result != hold:
                        hold = result
                        ret = iterator
                        
         return ret
              
        