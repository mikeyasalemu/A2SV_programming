class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        dic = defaultdict(int)
        count = 0
        add = 0
        
        for num in nums:
            add += num
            check = add - goal
            if check in dic:
                count += dic[check]
            if add == goal:
                count += 1
            
            dic[add] += 1 
        
        return  count