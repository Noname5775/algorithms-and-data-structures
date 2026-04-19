class Solution:
    def rob(self, nums):
        # Если домов нет, ответ равен 0
        if not nums:
            return 0

        # prev2 - максимум до дома i-2
        # prev1 - максимум до дома i-1
        prev2 = 0
        prev1 = 0

        for money in nums:
            # Либо не берём текущий дом,
            # либо берём его и добавляем сумму до дома i-2
            current = max(prev1, prev2 + money)
            prev2 = prev1
            prev1 = current

        return prev1