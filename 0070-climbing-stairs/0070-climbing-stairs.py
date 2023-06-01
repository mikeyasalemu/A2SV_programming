class Solution:
    def climbStairs(self, n: int) -> int:
        dic = {}
        dic[1] = 1
        if n == 1:
            return 1
        elif n == 2:
            return 2
        def DP(n):
            if n == 1:
                return 1
            if n == 2:
                return 2
            
            if n not in dic:
                dic[n] = DP(n -1) + DP (n -2)
            
            return dic[n]
        
        return DP(n)
        