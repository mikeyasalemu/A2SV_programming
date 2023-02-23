class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        right = 0
        avg = 0.0
        ans =0.0
        if k > len(nums):
            return 0
       
        while right < len(nums):
            if right < k:
                ans += nums[right]
                right +=1
                avg = ans
            else:
                avg = avg - nums[left] + nums[right]
                ans = max(ans, avg)
                right +=1
                left +=1
            
        return ans/k