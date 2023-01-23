class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        hold = int(len(piles) / 3)
        ans = 0
        piles.sort()
        index = -2
        for i in range(hold):
            ans+= piles[index]
            index+= -2
            
        return ans