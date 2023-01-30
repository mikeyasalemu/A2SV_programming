class Solution:
    def maxArea(self, height: List[int]) -> int:
        temp = 0
        right = len(height) - 1
        left = 0
        maximum = 0
        while left < right:
            if height[right] < height[left]:
                temp = height[right] * (right - left)
                maximum = max (maximum, temp)
                right -=1
            else:
                temp = height[left] * (right - left)
                maximum = max (maximum, temp)
                left +=1
        return maximum
            
        