class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        size = len(nums)
        nums = set(nums)
        for i in range(1,size+1):
            if i not in nums:
                ans.append(i)
        return ans