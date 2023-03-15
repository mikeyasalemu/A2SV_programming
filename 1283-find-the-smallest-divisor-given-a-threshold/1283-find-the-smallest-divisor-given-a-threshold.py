class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = max(nums)
        res = []

        while left < right:
            mid =(left+right)//2
            ans = 0
            for i in nums:
                ans+= math.ceil(i/mid)

            if ans <= threshold:
                right = mid
            elif ans > threshold:
                left = mid+1

        return left