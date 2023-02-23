class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        avg = 0.0
        ans =0.0
        if k > len(nums):
            return 0
        for i in range(k):
            ans += nums[i]

        avg = ans
        for i in range(k, len(nums)):
            avg += nums[i] - nums[i-k]
            ans = max(ans, avg)

        return ans/k