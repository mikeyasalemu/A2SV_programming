class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num1 = 0
        num2 = 0
        for i in nums:
            num1 = ~(num2) & (i ^num1)
            num2 = ~(num1) & (i ^ num2)
            
        return num1