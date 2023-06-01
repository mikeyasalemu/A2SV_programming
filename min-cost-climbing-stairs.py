class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dic = {}
        
        cost.append(0)
        def dp(ind):
            if ind >= len(cost):
                return 0
            if ind not in dic:
                dic[ind] = min(dp(ind+1), dp(ind+2)) + cost[ind]

            return dic[ind]

        return dp(-1)