class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.ans = []
        self.helper(1,n,k,[])
        
        return self.ans
    def helper(self,state,n,k,curr):
        if len(curr) == k:
            self.ans.append(curr)
            return 
        for i in range(state,n+1):
            self.helper(i+1,n,k,curr+[i])
            
            