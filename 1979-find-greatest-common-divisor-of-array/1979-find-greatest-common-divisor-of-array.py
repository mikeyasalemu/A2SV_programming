class Solution:
    def findGCD(self, nums: List[int]) -> int:
        num1 = min(nums)
        num2 = max(nums)
        return self.helper(num1,num2)
    
    def helper(self,num1,num2):
        if num2 == 0:
            return num1
        return self.helper(num2,num1%num2)