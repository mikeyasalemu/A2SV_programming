class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        rows, cols = len(dungeon), len(dungeon[0])
        dp = [([0] * cols) for _ in range(rows)]

        if dungeon[-1][-1] > 0:
            dp[-1][-1] = 1
        else:
            dp[-1][-1] = abs(dungeon[-1][-1]) + 1

        for row in range(rows - 1, -1, -1):
            for col in range(cols - 1, -1, -1):
                if dp[row][col] == 0:
                    bottom = right = float('inf')
                    if row + 1 < rows:
                        bottom = dp[row + 1][col]
                    if col + 1 < cols:
                        right = dp[row][col + 1]
                    
                    val = dungeon[row][col] - min(bottom, right)
                    
                    if val >= 0:
                        dp[row][col] = 1
                    else:
                        dp[row][col] = abs(val)

        print(dp)
        return max(1, dp[0][0])