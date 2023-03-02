class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        lst = [0]* (len(nums))
        for left, right in requests:
            lst[left] += 1
            if right+1 < len(nums):
                 lst[right+1] -=1
#         accumulate is an itertools which returns the prefixsum
        hold = sorted(list(accumulate(lst)))
        hold2 = sorted(nums)
        for i in range(len(hold)):
            hold[i]*= hold2[i]
        ans  = sum(hold)
                 
        return (ans % (pow(10,9) +7))
        
        