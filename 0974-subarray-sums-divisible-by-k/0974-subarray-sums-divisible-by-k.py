class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dic = defaultdict(int)
        dic[0] +=1
        count = 0
        pre = 0
        for num in nums:
            pre+= num
            temp = pre % k
            if temp in dic:
                count +=dic[temp]
            dic[temp] += 1
            
        return count