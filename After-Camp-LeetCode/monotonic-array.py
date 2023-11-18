class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1 or len(set(nums)) == 1:
            return True

        increase = True

        for i in range(1, len(nums)):
            if nums[i-1] != nums[i]:
                increase = nums[i-1] < nums[i]
                break
                
        ans = True
        for i in range(1, len(nums)):
            if not increase and nums[i-1] < nums[i]:
                ans = False
                break
            
            if increase and nums[i-1] > nums[i]:
                ans = False
                break
        return ans
