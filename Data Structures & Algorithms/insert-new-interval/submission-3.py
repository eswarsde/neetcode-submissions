class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:

        # Given intervals are already sorted 
        # Ideas: 
         #  1) maybe binary search to find the insertion sport quickly ??
         #  2) iterate one at a time, insert(merge any overlaps) and then just append the rest 


         # idea 2:

        insert_interval_start, insert_interval_end = newInterval

        result = []

        inserted = False

        for curr_start, curr_end in intervals: # already sorted by start 
            
            # case 1: insert interval before current interval [1, 2] [3, 4]
            if insert_interval_end < curr_start:
                if not inserted:
                    result.append([insert_interval_start, insert_interval_end])
                    inserted = True
                result.append([curr_start, curr_end])

            # case 2: insert interval after current interval [1, 2] [3, 4]
            elif curr_end < insert_interval_start:
                result.append([curr_start, curr_end])


            # case 3: insert interval overlaps current interval [1, 2] [2, 4]
            else:
                # don't merge with result yet. u don't know if the next interval is also a overlap
                insert_interval_start = min(curr_start, insert_interval_start)
                insert_interval_end = max(curr_end, insert_interval_end)
            
        if not inserted:
            result.append([insert_interval_start, insert_interval_end]) 

        return result