import heapq
from collections import defaultdict

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        # We want the cheapest cost to go from src to dst, but we can take at most k stops (so at most k+1 flights/edges).
        # Normal Dijkstra finds the cheapest path, but it ignores stop limits.
        # So we treat a "state" as: (current city, how many stops used).
        # That way, reaching the same city with different stop counts is considered different, and we can enforce the limit.
        

        # 1. Build Adjacency List
        adj_list = defaultdict(list)
        for u, v, price in flights:
             adj_list[u].append((v, price))

        # 2. State Tracker (The Secret Sauce)
        # We track the fewest STOPS it took to reach a node so far.
        min_stops = {}

        # 3. Min-Heap: Stores (cumulative_cost, current_city, stops_used)
        min_heap = [(0, src, 0)]

        while min_heap:
            current_cost, current_city, stops_used = heapq.heappop(min_heap)

            # # Target Check: The heap guarantees this is the cheapest valid path!
            if dst == current_city:
                return current_cost

            if stops_used > k:
                continue

            # Stale Path Check (Pruning):
            # # We already reached this city cheaper (popped earlier) AND with fewer/equal stops.
            # # This current path gives us absolutely no advantage, so throw it away
            if current_city in min_stops and min_stops[current_city] <= stops_used:
                continue

            # Lock in the new best stops for this city
            min_stops[current_city] = stops_used

            # 4. Edge Relaxation
            # When you pop a node off the heap, you look at all of its neighbors.
            for next_city, price in adj_list[current_city]:
                new_cost = current_cost + price
                heapq.heappush(min_heap, (new_cost, next_city, stops_used + 1))

        return -1

            



            

