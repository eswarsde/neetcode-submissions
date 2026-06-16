class Solution:
    # 853. Car Fleet - https://leetcode.com/problems/car-fleet/description/
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 1)  FIFO
          # A car can not pass another car ahead of it.
          # It can only catch up to another car and then drive at the same speed as the car ahead of it.
        # FIFO  - Stack

        """
         1. sort by position -> higest to lowest 
         2. calculate time each car takes
         3. start counting fleet
        """

        n = len(position)

        if n == 0:
            return 0

        cars = [(p,s) for p, s in zip(position, speed)] # (position, speed)
        # by defeault sorts using first entry in a tuple
        cars.sort(reverse=True)
        stack = []

        for p, s in cars:
            time = (target - p)/s


            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)    
