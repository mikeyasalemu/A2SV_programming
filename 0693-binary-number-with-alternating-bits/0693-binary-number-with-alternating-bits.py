class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        temp = 1&n
        n = n>>1
        ans = True
        while n > 0:
            # print(temp,n)
            if temp == 1&n:
                ans = False
                break
            else:
                temp = 1&n
            n = n>>1
        return ans