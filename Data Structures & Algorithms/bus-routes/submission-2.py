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
                        # The "Hub Stop" Optimization
                        if next_stop in visited_stops:
                            continue
                        visited_stops.add(next_stop)
                        queue.append(next_stop)
        return -1


        