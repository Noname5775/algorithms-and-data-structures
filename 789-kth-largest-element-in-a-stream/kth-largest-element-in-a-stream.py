import heapq
from typing import List

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []  # мин-куча
        for x in nums:
            heapq.heappush(self.heap, x)
            if len(self.heap) > k:
                heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        # Если элементов < k, корень всё равно хранит "k-ую" позицию
        return self.heap[0]