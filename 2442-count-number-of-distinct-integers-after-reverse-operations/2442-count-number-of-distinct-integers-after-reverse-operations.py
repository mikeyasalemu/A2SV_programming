class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
         size = len(nums)
         for i in range(size):
            n = str(nums[i])
            r = ""
            for i in n:
                r= i + r
            nums.append(int(r.lstrip('0')))
         nums.sort()
         # count = 1
         # for i in range(1,len(nums)):
         #        if nums[i -1] != nums[i]:
         #            count += 1
         return len(set(nums))
         