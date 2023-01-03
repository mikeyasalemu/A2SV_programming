import  numpy as np
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        size = len(nums)
        ans = []
        
        for index in range(size):
            num_index = nums[index]
            num = nums[num_index]
            ans.append(num)
        
        return ans