class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.append(0)
        n = len(nums)
        
        for idx in range(len(nums)):
            if nums[idx] < 0 or nums[idx] >= len(nums):
                nums[idx] = 0
        print(nums)
        for idx in range(len(nums)):
            nums[nums[idx] % n] += n
        print(nums)   
        for idx in range(1,len(nums)):
            if nums[idx] // n == 0:
                return idx
        
        
        
        return n
            