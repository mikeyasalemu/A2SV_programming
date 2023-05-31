class Solution:
    def fib(self, n: int) -> int:
        num1 = 0
        num2 = 1
        if n == 1:
            return 1
        elif n == 0:
            return 0
        
        for state in range(2,n+1):
            temp = num2
            num2 = temp + num1
            num1 = temp
        
        return num2