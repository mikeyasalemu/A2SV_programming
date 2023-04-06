class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        
        dic = defaultdict(int)
        temp = 0
        for i in nums:
            temp |= i
        # print(temp)
        self.count = 0
        self.helper(temp,nums,0,0)
        return self.count
    def helper(self,temp,nums,curr,ind):
        if curr == temp:
            self.count+=1
        for i in range(ind,len(nums)):
            hold = curr|nums[i]
            self.helper(temp,nums,hold,i+1)

            hold = curr
        return