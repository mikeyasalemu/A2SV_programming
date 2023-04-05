class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ch = []
        self.helper(0,nums,0)
        return self.ch
    
    def helper(self,state,nums,ch):        
        self.ch.append([])
        string = bin(ch)
        for i in range(len(string)-1,1,-1):
            if string[i] == '1':
                self.ch[-1].append(nums[len(string)-1-i])
        for i in range(state,len(nums)):
            temp = 1
            temp = temp<<i
            self.helper(i+1,nums,ch|temp)
        