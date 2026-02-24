import heapq
from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        heap = []  # мин-куча по частоте
        for num, f in freq.items():
            heapq.heappush(heap, (f, num))
            if len(heap) > k:
                heapq.heappop(heap)
        # извлекаем числа из кучи
        return [num for (_f, num) in heap]