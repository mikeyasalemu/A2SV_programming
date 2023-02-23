class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        summ = 0
        ans = float ('inf')
        while right < len(nums):
            if summ < target:
                summ += nums[right]
                
            if summ >= target:
                # print (left, right)
                ans = min(ans, right - left +1)
                if left < right:
                    
                    summ -= nums[left]
                    left+=1
                    # print (nums[left], nums[right], summ)
                    while left <= right and summ >= target:
                         
                         # print (nums[left])
                         if summ >= target:
                             # print (nums[left])
                             ans = min(ans, right - left+1)
                         summ -= nums[left] 
                         left+=1
                else:
                    summ+= nums[right]
                    
            if nums[right] >= target:
                ans = 1
                break
            right+=1
                    
        if ans == float('inf'):
            return 0
        return ans