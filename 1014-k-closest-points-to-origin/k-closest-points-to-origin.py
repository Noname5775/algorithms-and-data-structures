import heapq
from typing import List, Tuple

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap: List[Tuple[int, int, int]] = []  # будем хранить (-dist, x, y)
        for x, y in points:
            dist2 = x * x + y * y
            heapq.heappush(heap, (-dist2, x, y))
            if len(heap) > k:
                heapq.heappop(heap)
        # Оставшиеся в куче — k ближайших точек
        return [[x, y] for (_negd, x, y) in heap]