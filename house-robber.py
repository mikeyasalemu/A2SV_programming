class Solution:
    def rob(self, nums: List[int]) -> int:
        dic = {}

        def dp(ind):
            if ind == 0:
                return nums[0]
            elif ind == 1:
                return max(nums[0],nums[1])
            
            if ind not in dic:
                dic[ind] = max(dp(ind -1), dp(ind -2)+nums[ind])

            return dic[ind]
        
        return dp((len(nums) -1))