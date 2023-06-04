class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dic = defaultdict(int)

        def dp(ind, curr):
            if ind < 0 :
                if curr == target:
                    return 1
                return 0

            temp = (ind, curr)

            if temp not in dic:
                pos = dp(ind-1, curr+nums[ind])
                neg = dp(ind-1, curr-nums[ind])
                dic[temp] = pos + neg

                
            return dic[temp]

        return dp(len(nums) -1, 0)