class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # If there are 0 or 1 intervals, there is nothing to merge.
        if len(intervals) < 2:
            return intervals

        # Sort intervals by start time.
        # Python will use the end time as a tie-breaker.
        intervals.sort(key= lambda pair: pair[0]) # or simply intervals.sort() since by default sort is based on 0 index 

        # The first interval becomes our first merged interval.
        result = [intervals[0]]

        # Compare every remaining interval with the last merged interval.
        for curr_start, curr_end in intervals[1:]:

            # The last interval in result is the only interval
            # the current interval could overlap with.
            last_inserted_start, last_inserted_end = result[-1]

            # Overlap exists when the current interval starts
            # before or exactly when the previous interval ends.
            #
            # Example:
            # previous = [1, 4]
            # current  = [3, 6]
            if curr_start <= last_inserted_end:

                # Extend the previous interval's end boundary.
                #
                # We use max because the current interval may be
                # completely contained inside the previous interval.
                #
                # Example:
                # previous = [1, 10]
                # current  = [3, 5]
                # merged   = [1, 10], not [1, 5]
                last_inserted_end = max(last_inserted_end, curr_end)

                # Update the last merged interval in result.
                result[-1][1] = last_inserted_end

            else:
                # No overlap:
                # the current interval begins after the previous one ends,
                # so start a new merged interval.
                result.append([curr_start, curr_end])

        return result
        # Time complexity: O ( n log ⁡ n ) 
        # O(n) for the output list.

      
        # if len(intervals) <=1:
        #     return intervals

        # intervals.sort()
        # result = []

        # curr_start = intervals[0][0]
        # curr_end = intervals[0][1]

        # for i in range(1, len(intervals)):
        #     next_start = intervals[i][0]
        #     next_end = intervals[i][1]

        #     if next_start <= curr_end:
        #         currned_end = max(curr_end, next_end)
        #     else:
        #         result.append([curr_start, curr_end])
        #         curr_start = next_start
        #         currned_end = next_end
                

        # result.append([curr_start, curr_end])
        # return result