class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = str(x)
        ret = True
        a = len(y) - 1
        b = 0
        while a >= 0:
            if y[a] != y[b]:
                ret = False
            a -= 1
            b += 1
        return ret