class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        ans = 0
        size = len(nums)
        
        for ind,num in enumerate(nums):
            current = num
            j = ind
            while j < size and nums[j] % k == 0:
                current = math.gcd(current,nums[j])
                if current == k:
                    ans += 1
                j += 1
        return ans
