class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        size = len(nums)
        
#       to find the sum of consequative numbers
        ret = int(size*(size + 1)/2)
        for num in nums:
            ret -= num
        return ret
            