class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ans = 0
        temp = x^y
        return temp.bit_count()
        