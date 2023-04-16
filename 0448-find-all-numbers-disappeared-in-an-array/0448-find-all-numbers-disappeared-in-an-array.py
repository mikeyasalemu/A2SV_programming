class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        indx = 0
        ans = []
        while indx < len(nums):
            postionOfValue = nums[indx] - 1
            if postionOfValue != indx:
                if nums[postionOfValue] != nums[indx]:
                    nums[postionOfValue], nums[indx] = nums[indx], nums[postionOfValue]
                    continue
            indx+=1
        i = 0
        while i < n:
             correct_position = nums[i] - 1
             if correct_position != i:
                    ans.append(i+1)
             i+=1
            
            
        return ans