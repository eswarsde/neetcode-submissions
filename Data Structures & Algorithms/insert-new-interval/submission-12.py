class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:


        # Given intervals are already sorted 
        # Ideas: 
         #  1) maybe binary search to find the insertion sport quickly ??
         #  2) iterate one at a time, insert(merge any overlaps) and then just append the rest 


        # # idea 2 with for loop:

        # insert_interval_start, insert_interval_end = newInterval

        # result = []

        # inserted = False

        # for curr_start, curr_end in intervals: # already sorted by start 
            
        #     # case 1: insert interval after current interval [1, 2] [3, 4]
        #     if curr_end < insert_interval_start:
        #         result.append([curr_start, curr_end])

        #     # case 2: insert interval before current interval [1, 2] [3, 4]
        #     elif insert_interval_end < curr_start:
        #         if not inserted:
        #             result.append([insert_interval_start, insert_interval_end])
        #             inserted = True
        #         result.append([curr_start, curr_end])


        #     # case 3: insert interval overlaps current interval [1, 2] [2, 4]
        #     else:
        #         # don't merge with result yet. u don't know if the next interval is also a overlap
        #         insert_interval_start = min(curr_start, insert_interval_start)
        #         insert_interval_end = max(curr_end, insert_interval_end)
            
        # if not inserted:
        #     result.append([insert_interval_start, insert_interval_end]) 

        # return result

       # Time & Space Complexity:
       # Time complexity: O(n)
       # Space complexity: 
         # O(1) extra space.
         # O(n) space for the output list.        

         # idea 2  with while loop and simpler 

        # n = len(intervals)
        # i = 0
        # result = []
        # insert_interval_start, insert_interval_end = newInterval
   
        
        # while i < n and intervals[i][1] < insert_interval_start:
        #     result.append(intervals[i])
        #     i+=1
        
        # while i < n and insert_interval_end >= intervals[i][0]:
        #     insert_interval_start = min(insert_interval_start, intervals[i][0])
        #     insert_interval_end = min(insert_interval_end, intervals[i][1])
        #     i+=1
        # result.append([insert_interval_start, insert_interval_end])

        # while i < n:
        #     result.append(intervals[i])
        #     i+=1
        
        # return result

       # Time & Space Complexity:
       # Time complexity: O(n)
       # Space complexity: 
         # O(1) extra space.
         # O(n) space for the output list.

        # binary search - find the correct position where newInterval should be inserted based on its start time.

        if not intervals:
            return [newInterval]

        n = len(intervals)
        target = newInterval[0]
        left = 0
        right = n-1

        # Use binary search to find the correct position where newInterval should be inserted based on its start time.

        while left <= right:
            mid = (left + right) // 2

            if intervals[mid][0] < target:
                left = mid + 1
            else:
                right = mid - 1
        # After inserting, the list is still sorted by start time.
        intervals.insert(left, newInterval) # 0(n)
        
        # Iterating Through Intervals
        # Checking for No Overlap (The if condition)
        # 4. Merging Overlaps (The else condition)
        result = []
        for curr_start, curr_end in intervals:
            if not result or result[-1][1] < curr_start: # last interted interval end time < curr_start
                result.append([curr_start, curr_end])
            else:
                # overlap exists, so merge the end times, sort time is already sorted, so need to merge
                result[-1][1] = max(result[-1][1], curr_end)

        return result




