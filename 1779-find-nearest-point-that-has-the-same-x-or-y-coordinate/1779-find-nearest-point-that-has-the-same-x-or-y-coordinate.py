class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
         result  = float(inf)
         hold = result
         ret = -1
         valid = False
         for iterator,row in enumerate(points):
                # print (iterator, row)
                index1, index2 = row
                # print (index1, index2)
                if index1 == x or index2 == y:
                    valid = True
                    distance = abs( index1 - x)  + abs(y-index2)
                    result = min(distance , result)
                    if result != hold:
                        hold = result
                        ret = iterator
                        
               #    # print (abs(y - j))
                # if valid == False:
                #     result = -1
         return ret
              
        