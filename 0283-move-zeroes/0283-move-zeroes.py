class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        values = 0

        
        for  index in range(size):
            if nums[index] != 0:
                nums[values], nums[index] = nums[index], nums[values]
                values+=1
         
           
        return nums
            
            