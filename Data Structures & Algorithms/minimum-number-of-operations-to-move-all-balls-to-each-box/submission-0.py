class Solution:
    def minOperations(self, boxes: str) -> List[int]:

        # For any given index, you just need the answer to two questions:
        # The Left Side: How many '1's are to my left, and what is the total distance they have to travel to reach me?
        # The Right Side: How many '1's are to my right, and what is the total distance they have to travel to reach me?

        n = len(boxes)
        result = [0]*n

        # --- Pass 1: Left to Right ---
        # Calculate the cost to move all balls from the LEFT to the current box

        running_ball_count = 0
        running_ball_move_cost = 0
        for idx, box_val in enumerate(boxes):
            # 1. Store the accumulated moves before processing this box
            result[idx] += running_ball_move_cost

            # 2. Add the current box's ball (if it has one) to our total carrying count
            if box_val == '1':
                running_ball_count += 1

            # 3. Every ball we are carrying has to move one extra step for the next box
            # this keeps increasing whether bax_val is one or not - because the balls needs to move across all boxes
            running_ball_move_cost += running_ball_count


        running_ball_count = 0
        running_ball_move_cost = 0
        for idx in range(n - 1, -1, -1):
            # 1. Store the accumulated moves before processing this box
            result[idx] += running_ball_move_cost

            if boxes[idx] == "1":
                running_ball_count +=1

            running_ball_move_cost += running_ball_count
            
        return result


