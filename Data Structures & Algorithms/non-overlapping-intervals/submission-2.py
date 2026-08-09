class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)

        if n<=1:
            return 0
        # minimum number of meeting to remove
        # 

        intervals.sort(key=lambda interval: interval[1]) # O(n log n)

        prev_end_time = intervals[0][1]
        remove_count = 0

        for start, end in intervals[1:]:

            if start < prev_end_time: # overlap
                remove_count += 1
            else:
                prev_end_time = end # no overlap 

        return remove_count


        