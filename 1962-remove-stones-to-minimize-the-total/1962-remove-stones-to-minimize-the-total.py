class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        ans =  sum(piles)
        for i in range(len(piles)):
            piles[i] *=-1
        
        heapify(piles)
        
        while k > 0 and piles:
            temp = heappop(piles)
            
            ans -= (-temp//2)
            temp =-( ceil(-temp/2))
            
            if temp <= -2:
                heappush(piles,temp)
            k-=1
            
        return ans