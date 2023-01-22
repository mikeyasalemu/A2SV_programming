class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i], nums[red] = nums[red], nums[i]
                red+=1
        white = red
        for i in range(len(nums)):
            if nums[i] == 1:
                nums[i], nums[white] = nums[white], nums[i]
                white+=1
        