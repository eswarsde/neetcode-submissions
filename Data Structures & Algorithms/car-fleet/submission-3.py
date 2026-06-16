class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        """
        THE PROBLEM: 
        Cars are driving towards a target. Faster cars cannot pass slower cars; 
        they bump into them and form a "fleet", moving at the slower car's speed.
        How many distinct fleets cross the finish line?
        
        THE STRATEGY (Monotonic Stack):
        1. We don't simulate the driving. We calculate the "empty road time" 
           ((target - position) / speed) it would take each car to finish.
        2. We sort cars starting from the one closest to the target.
        3. GOLDEN RULE: If a car starts behind another car but has a FASTER OR EQUAL 
           time, it will catch up and join that car's fleet. It gets stuck, so 
           we throw its faster time away.
        4. If a car is SLOWER than the fleet ahead of it, it never catches up. 
           It forms a brand new fleet, so we add its time to our Stack.
        """
        
        n = len(position)
        if n == 0:
            return 0

        # Pair up (position, speed) and sort in reverse (closest to target first)
        cars = [(p, s) for p, s in zip(position, speed)] 
        cars.sort(reverse=True) 
        
        # Our stack (LIFO) to keep track of the slowest times leading each fleet
        fleet = []

        for p, s in cars:
            # Calculate how many hours this car takes to finish on an empty road
            time = (target - p) / s
            
            # If stack is empty OR this car is slower than the fleet ahead of it...
            if not fleet or time > fleet[-1]:
                # ...it cannot catch up. It becomes the leader of a brand new fleet!
                fleet.append(time)

        # The number of times in the stack equals the number of distinct fleets
        return len(fleet)