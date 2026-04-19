class Solution:
    def climbStairs(self, n: int) -> int:
        # dp[i] - количество способов добраться до i-й ступени
        if n <= 2:
            return n

        prev2 = 1  # dp[1]
        prev1 = 2  # dp[2]

        for i in range(3, n + 1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current

        return prev1