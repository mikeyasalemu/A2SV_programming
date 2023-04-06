class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num1 = 0
        num2 = 0
        ans = 0
        for i in range(len(nums)):
            nums[i]+=pow(2,31)
        for i in range(32):
            count = 0
            temp = 1
            temp <<= i
            for j in nums:
                if temp&j:
                    count+=1
            if count%3 > 0:
                ans+= pow(2,i)
            
        return ans-pow(2,31)