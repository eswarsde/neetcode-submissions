import heapq
from collections import defaultdict

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

 
        # # ### Standard Dijkstra vs. Modified Dijkstra (State Space Expansion)

        # # 1. Standard Dijkstra (The Baseline)
        # # In a standard shortest-path problem, Dijkstra's algorithm only cares about one thing: finding the absolute cheapest route to a physical location.

        # # * What goes in the heap: `(cumulative_cost, node)`
        # # * Why: The algorithm has a very short memory. If it finds a path to City B that costs $50, it completely overwrites and forgets a previous path to City B that cost $100. It doesn't care *how* many roads it took to get there, it only cares about the lowest price.

        # # 2. The Problem with Limits (e.g., "Within K Stops")
        # # If we apply standard Dijkstra to a problem with a stop limit, it will fail. It might find a super cheap $50 path to City B that takes 10 layovers, overwriting a $60 path that was a direct flight. If our limit was $K=1$ stop, standard Dijkstra just threw away our only valid answer!

        # # 3. Modified Dijkstra (State Space Expansion)
        # # To fix this, we have to change our definition of a "destination". We are no longer just traveling to "City B". We are traveling to a specific *state*: "City B using X stops".

        # # * What goes in the heap: `(cumulative_cost, current_node, stops_used)`
        # # * Why: By packing `stops_used` into our heap and state tracker, we force the algorithm to respect the constraint.
        # # * If a path pops out of the heap where `stops_used > limit`, we just `continue` and throw it away.
        # # * We now only prune (ignore) a path if we have already reached this exact city for a cheaper price AND using fewer (or equal) stops.



        # # ---

        # # The One-Sentence Summary:
        # # *"In standard Dijkstra, the heap only needs to track Cost and Node to find the cheapest physical route;
        # but when limits are introduced, we must expand our heap state to track Cost, Node, and Stops so we don't accidentally overwrite a slightly more expensive, but legally valid path."*

        # # We want the cheapest cost to go from src to dst, but we can take at most k stops (so at most k+1 flights/edges).
        # # Normal Dijkstra finds the cheapest path, but it ignores stop limits.
        # # So we treat a "state" as: (current city, how many stops used).
        # # That way, reaching the same city with different stop counts is considered different, and we can enforce the limit.
        

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
            if current_city in min_stops and stops_used >= min_stops[current_city]:
                continue

            # Lock in the new best stops for this city
            min_stops[current_city] = stops_used

            # 4. Edge Relaxation
            # When you pop a node off the heap, you look at all of its neighbors.
            for next_city, price in adj_list[current_city]:
                new_cost = current_cost + price


                 # No Eager Pruning & Update:
                 # If a problem has multiple competing limits (like Cost + Fuel, Cost + Stops, or Cost + Time Windows), you almost always have to abandon Eager Pruning and let the Min-Heap sort it out using Late Pruning instead!

                #  The reason we can't do Eager Pruning here boils down to one massive difference: Competing Constraints (Cost vs. Stops).

                #     In standard Dijkstra (Network Delay Time), you only care about ONE thing: Cost (Time).
                #     Because there is only one variable, you can be 100% certain that if new_cost > best_known_cost, that path is pure garbage. You can confidently throw it away before it ever touches the heap.

                #     In the Cheapest Flights problem, you are tracking a Two-Dimensional State: (Cost, Stops).

                heapq.heappush(min_heap, (new_cost, next_city, stops_used + 1))

        return -1

            


        # #  Bellman-Ford  can deal with negative  



        # # 1. Handle the trivial edge case
        # if src == dst:
        #     return 0

        # INF = math.inf
        
        # # 2. Initialize the costs array. 
        # # costs[i] represents the cheapest way to reach city i
        # costs = [INF] * n
        # costs[src] = 0

        # # 3. The core constraint: K stops means at most K + 1 flights
        # max_flights = k + 1

        # # 4. Run Bellman-Ford relaxations limited by our flight budget
        # for _ in range(max_flights): # kind of BFS 
        #     # Create a shallow copy for this specific iteration.
        #     # This prevents us from chaining multiple flights in a single "stop".
        #     temp_costs = costs.copy()

        #     # 5. Try relaxing every single available flight
        #     for u, v, price in flights:
        #         # If we can't even reach the departure city 'u', we can't take this flight
        #         if costs[u] == INF:
        #             continue

        #         # Calculate the cost of taking this specific flight
        #         candidate = costs[u] + price 

        #         # If it's cheaper than our current known best for this iteration, update it
        #         if candidate < temp_costs[v]:
        #             temp_costs[v] = candidate

        #     # 6. Commit the temporary costs for the next layer of flights
        #     costs = temp_costs

        # # 7. Return the destination cost, or -1 if it's still unreachable
        # return costs[dst] if costs[dst] != INF else -1



            

