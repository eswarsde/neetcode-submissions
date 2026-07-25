import heapq
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adj_list = defaultdict(list)
        for u, v, t in times:
            adj_list[u].append((v, t))

        distances = defaultdict(lambda: float('inf'))
        distances[k] = 0 # starting node's distance to 0 

        min_heap = [(0, k)]

        while min_heap:
            current_cost, u = heapq.heappop(min_heap)

            if current_cost > distances[u]:
                continue

            for v, t in adj_list[u]:
                new_cost = current_cost + t

                if new_cost < distances[v]:
                    distances[v] = new_cost
                    heapq.heappush(min_heap, (new_cost, v))

        max_time = max(distances.values())
        return int(max_time) if len(distances)==n else -1

        