class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        answer = []
        sum1 = 0
        for num in nums:
            if num % 2 == 0:
                sum1 += num
        
        for val, index in queries:
            
            if nums[index] % 2 == 0:
                sum1 -= nums[index]
            nums[index]+= val
            if nums[index] % 2 == 0:
                sum1 += nums[index]
            answer.append(sum1)
        return answer