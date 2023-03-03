class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        left = 0
        right = x // 2
        while left <= right:
            mid  = left + (right - left) // 2
            val = mid * mid
            if val < x:
                left = mid +1
            elif val > x:
                right = mid -1
            else:
                return mid
        if right * right <= x:
            return right
        elif left * left <= x:
            return left
        
            
                