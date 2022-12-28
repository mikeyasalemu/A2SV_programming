class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        
        for num in range(n, n*2, 2):
            if num % 2 == 0 and num % n == 0:
                return (num)
        return n*2