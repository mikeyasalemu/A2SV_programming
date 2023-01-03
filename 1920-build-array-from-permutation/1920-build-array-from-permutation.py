import  numpy as np
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        size = len(nums)
        ans = np.zeros(size, int)
        
        for index in range(size):
            
            ans[index] = nums[nums[index]]
        
        return ans