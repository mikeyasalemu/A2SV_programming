class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
         result  = float(inf)
         hold = result
         ret = -1
         for iterator,row in enumerate(points):
             
                if row[0] == x or row[1] == y:
                    distance = abs( row[0] - x)  + abs(y-row[1])
                    result = min(distance , result)
                    if result != hold:
                        hold = result
                        ret = iterator
                        
         return ret
              
        