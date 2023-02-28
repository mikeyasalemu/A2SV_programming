class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        arr = [0] * (len(nums) + 1)
        arr[0] =1 
        summ = 0
        ans = 0
        left = 0
        for i in range(len(nums)):
            if nums[i] % 2 != 0:
                summ += 1
            if summ >= k:
                ans += arr[summ - k]
            arr[summ] +=1
               
        return ans