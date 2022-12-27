class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        dic = defaultdict(lambda : 0)
        
        for intiger in nums:
            count += dic[intiger]
            dic[intiger] += 1
        
        return count