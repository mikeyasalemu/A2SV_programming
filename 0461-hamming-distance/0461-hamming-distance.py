class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        temp = x^y
        return temp.bit_count()
        """
        distance = 0
      while x > 0 or y > 0:
        if x & 1 != y & 1:
          distance += 1
        x >>= 1
        y >>= 1
      return distance
        """
        """
        return bin(x ^ y).count('1')
        """