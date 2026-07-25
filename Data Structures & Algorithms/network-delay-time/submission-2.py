import heapq
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        # We want the minimum time it takes for ALL nodes to receive the signal.
        # Since the signal travels simultaneously along all edges, the total time 
        # is simply the time it takes to reach the FURTHEST (or last) node.
        # Standard Dijkstra is perfect here: it finds the absolute shortest path to every node.

        # 1. Build Adjacency List
        # adj_list[node] = [(neighbor, travel_time)]
        adj_list = defaultdict(list)
        for u, v, t in times:
            adj_list[u].append((v, t))

       # 2. Distance Tracker
        # We track the absolute shortest known time to reach every node.
        # Using a defaultdict automatically returns infinity for any unseen node.     

        distances = defaultdict(lambda: float('inf'))
        distances[k] = 0 # starting node's distance to 0 

        # 3. Min-Heap: Stores (cumulative_cost, current_node)
        # The heap guarantees we always process the globally cheapest/fastest path next
        min_heap = [(0, k)]

        while min_heap:
            current_cost, u = heapq.heappop(min_heap)

            # Stale Path Check (Pruning):
            # If we already popped 'u' earlier with a shorter time, this current
            # heap entry is an older, slower path. Throw it away!
            if current_cost > distances[u]:
                continue

            # 4. Edge Relaxation
            # Look at all neighbors of the current node to see if we found a faster route.
            for v, t in adj_list[u]:
                new_cost = current_cost + t

                # Eager Pruning & Update:
                # Only record and push to the heap if this new path is STRICTLY faster
                # than the best time we've recorded for 'v' so far.

                if new_cost < distances[v]:
                    distances[v] = new_cost
                    heapq.heappush(min_heap, (new_cost, v))

# 5. Final Check
        # If len(distances) == n, we successfully reached every single server.
        # The time for ALL servers to receive the signal is the max time in our dictionary.

        max_time = max(distances.values())
        return int(max_time) if len(distances)==n else -1

# Time complexity: 
# O(ElogV)
# Space complexity: 
# O(V+E)

# # Where 

# V is the number of vertices and 

# E is the number of edges.