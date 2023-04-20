class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        check = set()
        for i in nums:
            prod = i
            d = 2
            while d * d <= prod:
                while prod % d == 0:

                    check.add(d)
                    prod //= d

                d+=1
            if prod!= 1:
                check.add(prod)
        
        return len(check)