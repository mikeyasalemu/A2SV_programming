import  numpy as np
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        size = len(nums)
        ans = []
        
        for index in range(size):
            
            ans.append(nums[nums[index]])
        
        return ans