import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times, n, k):
        # Список смежности: вершина -> [(сосед, вес), ...]
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        # Расстояния до всех вершин: сначала бесконечность
        dist = {i: float('inf') for i in range(1, n + 1)}
        dist[k] = 0

        # Очередь с приоритетом: (расстояние, вершина)
        heap = [(0, k)]

        while heap:
            cur_dist, node = heapq.heappop(heap)

            # Если нашли устаревшее значение, пропускаем
            if cur_dist > dist[node]:
                continue

            for neighbor, weight in graph[node]:
                new_dist = cur_dist + weight

                # Если нашли более короткий путь, обновляем
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    heapq.heappush(heap, (new_dist, neighbor))

        max_dist = max(dist.values())

        return max_dist if max_dist != float('inf') else -1