class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        temp = [nums[i] for i in range(len(nums))]
        # print(temp)
        self.helper(ans,nums,0,temp)
        return ans
    def helper(self,ans,nums,ind,temp):
        
        if ind == len(nums):
            # print(temp)
            ans.append(temp)
            return
        for i in range(ind,len(nums)):
            temp[ind],temp[i]= temp[i],temp[ind]
            self.helper(ans,nums,ind+1,temp[:])
            temp[ind],temp[i]= temp[i],temp[ind]
            # temp[i] = nums[i]
            # temp[ind] = nums[ind]
            # print(temp)
            