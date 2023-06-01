class Solution:
    def climbStairs(self, n: int) -> int:
        state = [0] * (n + 1)
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        state[1] = 1
        state[2] = 2
        
        
        for i in range(3,n+1):
            state[i] = state[i -1] + state[i -2]
        
        return state[-1]