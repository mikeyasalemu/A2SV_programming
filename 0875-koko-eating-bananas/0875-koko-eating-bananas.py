class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        while left < right:
            mid =(left+right)//2
            ans = 0
            for i in piles:
                ans+= math.ceil(i/mid)

            if ans <= h:
                right = mid
            elif ans > h:
                left = mid+1

        return left