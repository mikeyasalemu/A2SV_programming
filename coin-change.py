class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dic = {0:0}
        def dp(target):
            if target in dic:
                return dic[target]
            if target < 0:
                return float("inf")
            temp = float("inf")
            for coin in coins:
                temp = min(temp, dp(target - coin))
            dic[target] = temp+1

            return dic[target]
        ans = dp(amount)
        if  ans == float("inf"):
            return -1
        return ans