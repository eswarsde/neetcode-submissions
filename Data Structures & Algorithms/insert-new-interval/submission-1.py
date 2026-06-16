class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        # Unpack the new interval into start and end values
        new_start, new_end = newInterval

        # This will hold the final list of intervals after insertion/merging
        merged: list[list[int]] = []

        # Tracks whether we have already inserted the new interval
        inserted = False

        # Go through each existing interval one by one
        for start, end in intervals:
            # Case 1:
            # Current interval is completely before the new interval
            # Example: current = [1, 2], new = [5, 7]
            # Since there is no overlap, just add it as-is
            if end < new_start:
                merged.append([start, end])

            # Case 2:
            # Current interval is completely after the new interval
            # Example: current = [10, 12], new = [5, 7]
            # If we have not yet inserted the new interval, do it now
            # Then add the current interval
            elif start > new_end:
                if not inserted:
                    merged.append([new_start, new_end])
                    inserted = True

                merged.append([start, end])

            # Case 3:
            # Current interval overlaps with the new interval
            # Example: current = [3, 5], new = [4, 7]
            # Merge by expanding new_start and new_end
            else:
                new_start = min(new_start, start)
                new_end = max(new_end, end)

        # If the new interval was never inserted, it means:
        # - it belongs at the end, or
        # - it merged through the final interval(s)
        if not inserted:
            merged.append([new_start, new_end])

        # Return the final merged interval list
        return merged

        