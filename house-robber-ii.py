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
        
        if len(nums) == 1:
            return nums[0]
        
        ans1 = dp((len(nums) -2))
        nums[0] = 0
        dic = {}
        ans2 = dp((len(nums) -1))
    
        return max(ans1,ans2)