class Solution:
    def missingNumber(self, nums: List[int]) -> int:
       
        ret = int( len(nums)*( len(nums) + 1)/2)
        for num in nums:
            ret -= num
        return ret
            