from collections import deque, defaultdict 
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int: 

        # Model this problem as Graph (Stops as nodes)
        # Least number of buses - BFS
        # Input -> list of List

        if source == target:
            return 0
        
        # What the input gives you (Bus -> Stops)
        # What the map gives you (Stop -> Buses)
        # To successfully run a BFS, you have to alternate between these two states: Take a bus -> Get off at a stop -> Check available buses -> Take a new bus.
        # Imagine you are at Stop 5 and you want to know which buses you can transfer to.
        #  Without the map: You would have to loop through every single bus route in the entire input array and check if Stop 5 is inside it.
        stop_to_buses = defaultdict(list)
        for bus_id, bus_stop_list in enumerate(routes):
            for stop in bus_stop_list:
                stop_to_buses[stop].append(bus_id)
        
        if source not in stop_to_buses or target not in stop_to_buses:
            return -1
        
        bus_taken_count = 0
        queue = deque([source])
        visited_stops = {source}
        visited_buses = set()
        while queue:
            num_stops_at_level = len(queue)
            bus_taken_count += 1

            # In a standard matrix BFS, a "level" is one physical step in a direction.In this problem, one level equals one bus ride.
            # Process one full "level" (one bus ride)
            for _ in range(num_stops_at_level):
                current_stop = queue.popleft()

                # 1. Look at all buses arriving at this stop
                for bus_id in stop_to_buses[current_stop]:

                    # 2. Skip buses we have already ridden
                    # Prevents Infinite Loops, Ensure you never board the same bus twice.
                    if bus_id in visited_buses:
                        continue
                    visited_buses.add(bus_id)

                    # 3. For every new bus, look at all the stops it goes to
                    for next_stop in routes[bus_id]:
                        # Did we reach the destination?
                        if next_stop == target:
                            return bus_taken_count

                        # 4. Skip stops we have already visited
                        # Mark as visited and queue it up for the next level!
                        # Why we need visited_stops

                        ### 2. `visited_stops`: The "Hub Stop" Optimization

                        # **The Goal:** Prevent redundant dictionary lookups at highly congested transit centers.

                        # This is the hidden performance killer that causes the $O(N \cdot K \cdot N)$ Time Limit Exceeded (TLE) error we discussed earlier.

                        # Imagine **Stop 5** is a massive central transit hub where **100 different bus routes** intersect.

                        # * **Without `visited_stops`:**
                        # * You board the 1st bus that goes through Stop 5. You loop through its stops, hit Stop 5, and use `stop_to_buses[5]` to fetch all 100 connecting buses. You check each of those 100 buses to see if they are in `visited_buses`.
                        # * Later, you board the 2nd bus that goes through Stop 5. You hit Stop 5 again. You fetch the *exact same* list of 100 connecting buses. You do those 100 checks all over again.
                        # * By the time you process all buses passing through that hub, your code will have scanned that same 100-bus list up to 100 times, resulting in **10,000 redundant check operations** for a single stop!


                        # * **With `visited_stops`:**
                        # * The very first time a bus reaches Stop 5, you add Stop 5 to `visited_stops`, queue it up, and check its 100 connections.
                        # * When the 2nd, 3rd, and 100th buses reach Stop 5, the `if next_stop in visited_stops:` check instantly skips it. You never fetch that massive 100-bus list again.



                        if next_stop in visited_stops:
                            continue
                        visited_stops.add(next_stop)
                        queue.append(next_stop)
        return -1


        