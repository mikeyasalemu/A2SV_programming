class Solution:
    def myPow(self, x: float, n: int) -> float:
        temp = n
        
        ans = self.calc(x, abs(n))
        
        if temp < 0:
            return 1/ans
        else:
            return ans
    
    def calc(self,x,n):
        if x == 0:
            return 0
        elif n == 0:
            return 1
        
        res = self.calc(x, n//2)
        
        if n % 2:
            return res*res *x
        else:
            return res*res
            