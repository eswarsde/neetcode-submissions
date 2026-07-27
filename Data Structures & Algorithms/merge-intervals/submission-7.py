class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Input: intervals = [[1,3],[1,5],[6,7]]
        # Output: [[1,5],[6,7]]

        # o(n log n)
        intervals.sort(key= lambda x: x[0])

        result = [intervals[0]]

        for current_start, current_end in intervals[1:]:
            prev_start, prev_end = result[-1]

            if current_start <= prev_end:
                prev_end = max(current_end, prev_end)
                result[-1][1] = prev_end
            else:
                result.append([current_start, current_end])
 
    
        return result