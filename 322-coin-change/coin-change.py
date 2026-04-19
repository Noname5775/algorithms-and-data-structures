class Solution:
    def coinChange(self, coins, amount):
        # dp[x] - минимальное число монет для суммы x
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for x in range(1, amount + 1):
            for coin in coins:
                if x - coin >= 0:
                    dp[x] = min(dp[x], dp[x - coin] + 1)

        return -1 if dp[amount] == float('inf') else dp[amount]