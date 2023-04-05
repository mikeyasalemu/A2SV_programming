class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.ch = []
        self.helper(0,nums,[],0)
        # print(1<<0)
        # print(bin(2))
        print(self.ch)
        return self.ch
    
    def helper(self,state,nums,curr,ch):
        self.ans.append(curr)
        
        self.ch.append([])
        string = bin(ch)
        
        for i in range(len(string)-1,1,-1):
            if string[i] == '1':
                self.ch[-1].append(nums[len(string)-1-i])
        print(ch,string,self.ch[-1])
        for i in range(state,len(nums)):
            temp = 1
            temp = temp<<i
            self.helper(i+1,nums,curr+[nums[i]],ch|temp)
        