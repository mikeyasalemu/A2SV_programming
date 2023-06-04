class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        
        dic = [0]*(n+1)
        
        if n == 0:
            return 0
        elif n == 1:
            return 1

        dic[0] = 0
        dic[1] = 1
        ans = 0
        for i in range(2,n+1):
            if i % 2 == 0:
                dic[i] = dic[int(i/2)]
            else:
                dic[i] = dic[math.ceil(i/2)] + dic[math.floor(i/2)]
        
        return max(dic)