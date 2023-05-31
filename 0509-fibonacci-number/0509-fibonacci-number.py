class Solution:
    def fib(self, n: int) -> int:
        dic = {}
        
        def dp(n):
            if n == 0:
                return 0
            if n == 1:
                return 1
            
            if n not in dic:
                dic[n] = dp(n-1)+dp(n-2)
            
            return dic[n]
        
        return  dp(n)