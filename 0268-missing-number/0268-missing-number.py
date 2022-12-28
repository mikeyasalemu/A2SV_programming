class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        sets = set(nums)
        size = len(sets)
#       to find the sum of consequative numbers
        # ret = int(size*(size + 1)/2)
        for num in range(size +1):
            if num not in sets:
                return num
        return 1
            