class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        sets = set(nums)
        size = len(sets)
        
#       to find the number that is not in the given set of list
        for num in range(size +1):
            if num not in sets:
                return num
        return 1
            