class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.check = set()
        self.helper(0,nums,[])
        # print(self.check)
        return self.ans
    def helper(self,state,nums,curr):
        if len(curr) > 1 and tuple(curr) not in self.check:
            self.ans.append(curr)
            self.check.add(tuple(curr))
        i = state
        while i < len(nums):
            if not curr or i > 0  and curr and nums[i] >= curr[-1]:
                self.helper(i+1,nums,curr+[nums[i]])
            
            i+=1
                
                
            # if i + 1 <= len(nums)-1 and nums[i] == nums[i+1]:
                
                
            # curr.pop()
            # curr.pop()
            