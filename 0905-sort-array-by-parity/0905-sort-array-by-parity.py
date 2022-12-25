class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        hold = 0
        size = len(nums)
        even_index = 0
        for index in range(size):
            if nums[index] % 2 == 0:
                hold = nums[index]
                nums.pop(index)
                nums.insert(even_index, hold)
                even_index +=1
        return nums
                
                