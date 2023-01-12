class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        size = len(nums)
        index = 0
        if len(nums) == 1:
            return nums
        while index < size -1:
            if nums[index] == nums[index +1]:
                nums[index]*= 2
                nums[index +1] =0
                index+=1
            index+=1
            
        ans = [0]*size
        index = 0
        for element in nums:
            if element != 0:
                ans[index] = element
                index+=1
                 
                
        return ans