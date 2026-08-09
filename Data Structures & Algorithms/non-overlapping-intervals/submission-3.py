class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)

        if n<=1:
            return 0
        # minimum number of meeting to remove
        
        intervals.sort(key=lambda interval: interval[1]) # O(n log n)

        last_inserted_end = intervals[0][1]
        remove_count = 0

        for curr_start, curr_end in intervals[1:]:

            if curr_start < last_inserted_end: # overlap
                remove_count += 1
            else:
                last_inserted_end = curr_end # no overlap 

        return remove_count


        