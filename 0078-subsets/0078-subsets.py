class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.helper(0,nums,[])
        
        return self.ans
    def helper(self,state,nums,curr):
        self.ans.append(curr)
        for i in range(state,len(nums)):
            self.helper(i+1,nums,curr+[nums[i]])
        