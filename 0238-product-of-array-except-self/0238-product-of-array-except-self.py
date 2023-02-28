class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left =[1]*(len(nums) +1)
        right = [1]*(len(nums) +1)
        for i in range(1,len(nums)+1):
            left[i] = left[i - 1]* nums[i -1]
        for i in range(len(nums) -1, -1, -1):
            right[i] = right[i +1] * nums[i]
        # print (right , left)
        for i in range(len(nums)):
            nums[i] = left[i] * right[i+1]
        # print (nums)
        return nums