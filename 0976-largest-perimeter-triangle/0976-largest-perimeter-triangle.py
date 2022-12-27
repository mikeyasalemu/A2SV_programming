class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        """first reverse of the numbers and check if the number in the left is grater th the             others""" 
    
        nums.sort(reverse = True)
        
        size = len(nums)
        for index in range(size -2):
            num1 = nums[index]
            num2 = nums[index + 1]
            num3 = nums[index + 2]
            if num1 < num2 + num3:
                return num1 + num2 + num3
            
        return 0
        