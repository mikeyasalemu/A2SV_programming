class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        size = len(heaters)
        ans = 0
        
        houses.sort()
        heaters.sort()
        
        for i in range(len(houses)):
            left = 0
            left = bisect_left(heaters, houses[i], 0, size -1)
            
            # right = bisect_right(heaters, houses[i], 0, size -1)
            
            if left == 0:
                left_ans = abs(heaters[0] - houses[i])
            else:
                left_ans = min(abs(heaters[left] - houses[i]), abs(heaters[left -1] - houses[i]))
            
            ans = max(ans, left_ans)
            # print(houses[i], ans, heaters[left])
            
        # print(bisect_left(heaters, 2, 0, size -1))
        return ans
        
        