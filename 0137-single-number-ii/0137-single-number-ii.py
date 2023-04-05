class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = Counter(nums)
        for i in nums:
            if dic[i] == 1:
                ans = i
                break
        return ans