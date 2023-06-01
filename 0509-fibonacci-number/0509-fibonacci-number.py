class Solution:
    def fib(self, n: int) -> int:
        num1 = 0
        num2 = 1
        
        if n == 0:
            return 0

        elif n == 1:
            return 1
        
        for i in range(2, n+1):
            
            temp = num2
            num2 = num1 + num2
            num1 = temp
       
        
        return  num2