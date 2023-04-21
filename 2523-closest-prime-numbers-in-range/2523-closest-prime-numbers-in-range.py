class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        prime = [True for i in range(right+1)]
        
        d = 2
        
        while d * d <= right:
            
            if prime[d]:
                for i in range(d*d , right+1, d):
                    prime[i] = False
            d+=1
        ans = []
        for i in range(len(prime)):
            if i > 1 and  i >= left and prime[i] == True:
                ans.append(i)
        
        if len(ans) < 2:
            return [-1, -1]
        dic2 = defaultdict(int)
        minn = float('inf')
        for i in range(len(ans) -1):
            dic2[i] = abs(ans[i] - ans[i+1])
            minn = min(minn ,abs(ans[i] - ans[i+1]))
        for num,val in dic2.items():
            if val == minn:
                return [ans[num] , ans[num+1]]
       