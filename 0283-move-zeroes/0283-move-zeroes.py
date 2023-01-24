class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        values = 0
        index = values + 1

        
        while index < size:
            
            if nums[values] == 0 and nums[index] != 0:
                nums[values], nums[index] = nums[index], nums[values]
                values +=1
                index +=1
            elif nums[values] == 0 and nums[index] == 0:
                index +=1
            else:
                values +=1
                index +=1
                
        return nums
            
            