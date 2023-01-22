class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        newNums = sorted(nums)
        c = {}
        res = []
        for i in range(len(nums)):
            if newNums[i] not in c:
                c[newNums[i]] = i
        for n in nums: 
            res.append(c[n])
        return res
                
        
        