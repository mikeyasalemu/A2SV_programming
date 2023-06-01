class Solution:
    def tribonacci(self, n: int) -> int:
        dic = {}

        def DP(n):
            if n == 0:
                return 0
            if n == 2:
                return 1
            if n == 1:
                return 1
            if n not in dic:
                dic[n] = DP(n-1)+DP(n-2)+DP(n-3)
            return dic[n]
            
        return DP(n)