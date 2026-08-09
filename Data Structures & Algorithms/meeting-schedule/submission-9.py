"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) <= 1:
            return True

        intervals.sort(key=lambda interval: interval.start)
        
        # Track the end time of the last meeting we "attended"
        last_attended_end = intervals[0].end

        for interval in intervals[1:]:
            curr_start = interval.start
            curr_end = interval.end

            if curr_start < last_attended_end: # overlap 
                return False
            else:
                last_attended_end = curr_end

        return True

# Time complexity: O(nlogn)
# Space complexity: O(1) or O(n) depending on the sorting algorithm.