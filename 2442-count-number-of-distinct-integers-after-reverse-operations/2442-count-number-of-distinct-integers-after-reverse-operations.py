class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
         size = len(nums)
         for i in range(size):
            n = str(nums[i])
            r = ""
            for i in n:
                r= i + r
            nums.append(int(r.lstrip('0')))
         nums = set(nums)
         return len(nums)
         