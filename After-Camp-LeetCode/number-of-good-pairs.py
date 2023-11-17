class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        dic = defaultdict(int)
        
#      assign defaltdict and count the pairs from getting the previous 
#          dictionary value
        for intiger in nums:
            count += dic[intiger]
            dic[intiger] += 1
        
        return count