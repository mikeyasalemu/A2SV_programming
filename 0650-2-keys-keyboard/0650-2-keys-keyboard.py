class Solution:
    def minSteps(self, n: int) -> int:
        if n ==1 :
            return 0
        d= 2
        lst = []
        ans = 0
        while d * d <= n:
            while n % d == 0:
                lst.append(d)
                # print(d)
                n//=d
            d+=1
        # print(3%2)
        if n != 1:
            lst.append(n)
        # print(lst)
        ans = sum(lst)
        # print(ans)
        return ans