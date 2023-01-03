class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        size = len(nums)
        ans = []
        
        for index in range(0, size):
            
            ans.append(nums[nums[index]])
        
        return ans