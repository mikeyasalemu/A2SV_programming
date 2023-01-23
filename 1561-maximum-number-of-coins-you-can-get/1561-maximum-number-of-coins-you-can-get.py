class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        hold = len(piles) // 3
        ans = 0
        piles.sort()
        index = -2
        i = 0
        while i < hold:
            ans+= piles[index]
            index+= -2
            i+=1
            
        return ans