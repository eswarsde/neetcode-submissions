"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        # Approach 1: 
        # if you think about this problem, at any given point in time, we need to know the room that's about to finsih the earliest
        # we can keep that end time in a heap, specifically min heap, which keeps the smallest/earliest end time at the top to peek
        # if at a given time, there is no empty room, I guess you can insert the end time of the current meeting in the heappop


        # intervals.sort(key=lambda x: x.start)

        # min_heap = []

        # for interval in intervals:

        #     ## current meeting rooms can accomdate the next meeting
        #     if min_heap and min_heap[0] <= interval.start:
        #         heapq.heappop(min_heap)

        #     heapq.heappush(min_heap, interval.end)

        # return len(min_heap)

        # Time complexity: O(nlogn)
        # Space complexity: O(n)


        # Approach 2: The Sweep Line Algorithm using dictionary 

#         To really understand *why* this works, it helps to step away from the code for a second and think about a real-world analogy.

            # ### The Real-World Analogy: A Building Lobby

            # Imagine you are standing at the front door of a building holding a clicker counter. Your goal is to find out the **maximum number of people inside the building at the exact same time** today.

            # You don't care *who* the people are. You don't care *how long* they stay. You only care about two events:

            # 1. Someone walks **in** (the building gains a person: `+1`).
            # 2. Someone walks **out** (the building loses a person: `-1`).

            # If you start at 0 and just press `+1` every time someone enters, and `-1` every time someone leaves, the highest number you ever see on your clicker is the maximum capacity you needed that day.

            # This is exactly what the Sweep Line algorithm is doing with meeting rooms.

            # ---

            # ### Breaking Down the Code's Logic

            # #### 1. The Dictionary (`room_changes = defaultdict(int)`)

            # Why use a dictionary instead of just a list of events? Because of traffic jams at the door.

            # Imagine at exactly 10:00 AM, one person walks out, and another person walks in.

            # * Walk out = `-1`
            # * Walk in = `+1`
            # * Net change = `0`

            # The dictionary automatically handles this math for us. If `Meeting A` ends at 10 and `Meeting B` starts at 10, `room_changes[10]` calculates `-1 + 1 = 0`. This perfectly represents that the room just seamlessly changed hands, and we didn't need to open a brand new one.

            # #### 2. Sorting the Keys (`for time in sorted(room_changes.keys()):`)

            # To know how many rooms are in use at any given moment, you *must* process the events in chronological order. You can't process a 2:00 PM event before an 11:00 AM event.

            # By sorting the unique times, we are effectively walking the timeline from morning to night, pausing only at the exact moments when a meeting starts or ends.

            # #### 3. Tracking the Peak (`max_rooms_needed = max(...)`)

            # As we walk the timeline, we keep a running total (`current_active_rooms`). Because we only care about the absolute worst-case scenario (the busiest moment of the day), we constantly update our "high score" (`max_rooms_needed`).

            # ---

            
        room_changes = defaultdict(int)

        # Step 1: Log the events onto the timeline
        for interval in intervals:
            room_changes[interval.start] += 1  # Meeting starts, open a room
            room_changes[interval.end] -= 1    # Meeting ends, free a room

        active_rooms = 0
        max_rooms = 0

        for time in sorted(room_changes.keys()):

            active_rooms += room_changes[time]
            max_rooms = max(max_rooms, active_rooms)

        return max_rooms

        # # Approach 3: 

        # starts = sorted([i.start for i in intervals])
        # ends = sorted([i.end for i in intervals])

        # i = 0  # Pointer for the starts list (next meeting to start)
        # j = 0  # Pointer for the ends list (next meeting to end)
        # rooms_in_use = 0  # Number of rooms currently occupied by active meetings
        # max_rooms = 0  # Maximum number of rooms needed at any point in time

        # n = len(intervals)  # Total number of intervals, used as loop bound

        # # Sweep over the timeline using the start and end events
        # while i < n:  # Continue until we have processed all start times
        #     # If the next meeting starts before the earliest current meeting ends
        #     if starts[i] < ends[j]:  # Strict < means equal times don't count as overlap
        #         rooms_in_use += 1  # A new meeting starts, so we need one more room
        #         if rooms_in_use > max_rooms:  # Check if we have reached a new peak
        #             max_rooms = rooms_in_use  # Update the maximum number of rooms
        #         i += 1  # Move to the next start time
        #     else:
        #         # Otherwise, previous meeting ends before or at the same time as the next start
        #         # so the room is free for this/next meeting
        #         rooms_in_use -= 1  # A meeting ended, so one room becomes free
        #         j += 1  # Move to the next end time

        # return max_rooms  # Return the maximum rooms that were in use at any time
