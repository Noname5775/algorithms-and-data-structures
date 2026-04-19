class Solution:
    def canPartition(self, nums):
        total = sum(nums)

        # Если сумма нечётная, разделить на две равные части нельзя
        if total % 2 != 0:
            return False

        target = total // 2

        # dp[s] - можно ли получить сумму s
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            # Идём с конца, чтобы не использовать одно и то же число дважды
            for s in range(target, num - 1, -1):
                dp[s] = dp[s] or dp[s - num]

        return dp[target]