from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Мин-куча размера k: корень — k-ый по величине элемент
        heap = []
        for x in nums:
            heapq.heappush(heap, x)
            if len(heap) > k:
                heapq.heappop(heap)
        # Теперь heap[0] — k-ый наибольший
        return heap[0] 