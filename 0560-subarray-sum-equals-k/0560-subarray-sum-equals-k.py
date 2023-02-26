class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = defaultdict(int)
        count = 0
        add = 0
        
        for num in nums:
            add += num
            check = add - k
            if check in dic:
                count += dic[check]
            if add == k:
                count += 1
            
            dic[add] += 1 
        
        return  count