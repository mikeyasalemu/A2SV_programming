class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        ans2 = []
        self.helper(ans,ans2,nums,0,0)
        return ans
    def helper(self,ans,ans2,nums,ind,num):
        
        if ind == len(nums):
            ans.append(ans2)
            return
        for i in range(len(nums)):
            if not num&(1<<i):
                self.helper(ans,ans2+[nums[i]],nums,ind+1,num|(1<<i))
            
            