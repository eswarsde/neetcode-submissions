"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
#import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        # intervals.sort(key=lambda x: x.start)

        # min_heap = []

        # for interval in intervals:

        #     ## current meeting rooms can accomdate the next meeting
        #     if min_heap and min_heap[0] <= interval.start:
        #         heapq.heappop(min_heap)

        #     heapq.heappush(min_heap, interval.end)

        # return len(min_heap)

        starts = sorted([i.start for i in intervals])
        ends = sorted([i.end for i in intervals])

        i = 0  # Pointer for the starts list (next meeting to start)
        j = 0  # Pointer for the ends list (next meeting to end)
        rooms_in_use = 0  # Number of rooms currently occupied by active meetings
        max_rooms = 0  # Maximum number of rooms needed at any point in time

        n = len(intervals)  # Total number of intervals, used as loop bound

        # Sweep over the timeline using the start and end events
        while i < n:  # Continue until we have processed all start times
            # If the next meeting starts before the earliest current meeting ends
            if starts[i] < ends[j]:  # Strict < means equal times don't count as overlap
                rooms_in_use += 1  # A new meeting starts, so we need one more room
                if rooms_in_use > max_rooms:  # Check if we have reached a new peak
                    max_rooms = rooms_in_use  # Update the maximum number of rooms
                i += 1  # Move to the next start time
            else:
                # Otherwise, a meeting ends before or at the same time as the next start
                rooms_in_use -= 1  # A meeting ended, so one room becomes free
                j += 1  # Move to the next end time

        return max_rooms  # Return the maximum rooms that were in use at any time
