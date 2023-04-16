class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ind = 0
        ans = []
        while ind < len(nums):
            val = nums[ind]-1
            if val != ind:
                if nums[val] != nums[ind]:
                    nums[val],nums[ind] = nums[ind],nums[val]
                    continue
            ind+=1
        ind = 0
        while ind < len(nums):
            val = nums[ind] -1
            if val != ind:
                ans.append(nums[ind])
            ind +=1
        return ans
#         n = len(nums)
#         indx = 0
#         ans = []
#         while indx < len(nums):
#             postionOfValue = nums[indx] - 1
#             if postionOfValue != indx:
#                 if nums[postionOfValue] != nums[indx]:
#                     nums[postionOfValue], nums[indx] = nums[indx], nums[postionOfValue]
#                     continue
#             indx+=1
#         i = 0
#         while i < n:
#              correct_position = nums[i] - 1
#              if correct_position != i:
#                     ans.append(nums[i])
#              i+=1
            
            
#         return ans
        