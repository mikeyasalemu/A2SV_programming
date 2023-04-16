class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        size = len(nums)
        left = 1
        right = size
        
        while left < right:
            middle = left + (right - left)//2
            count = 0

            for i in range(size):
                if nums[i] <= middle:
                    count += 1
            
            if count > middle:
                right = middle
            else:
                left = middle+1

        return left