class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        count = 0
        size = len(nums)
        
        for index,num in enumerate(nums):
            current = num
            j = index
            while j < size and nums[j] % k == 0:
                current = math.gcd(current,nums[j])
                if current == k:
                    count += 1
                j += 1
        return count
