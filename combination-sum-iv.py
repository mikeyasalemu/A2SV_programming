class Solution:
    def combinationSum4(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dic = {0:0}
        def dp(target):
            if target == 0:
                return 1
            if target in dic:
                return dic[target]
            temp = 0
            for coin in coins:
                if target - coin >=  0:
                    temp += dp(target - coin)
            dic[target] = temp

            return dic[target]
        ans = dp(amount)
        
        return ans