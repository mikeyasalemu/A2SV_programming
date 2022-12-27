class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        size = len(nums)
        for index in range(size +1):
            if index not in nums:
                return (index)