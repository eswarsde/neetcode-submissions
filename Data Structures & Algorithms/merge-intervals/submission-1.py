class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <=1:
            return intervals

        intervals.sort()
        results = []

        current_start = intervals[0][0]
        currned_end = intervals[0][1]

        for i in range(1, len(intervals)):
            next_start = intervals[i][0]
            next_end = intervals[i][1]

            if next_start <= currned_end:
                currned_end = max(currned_end, next_end)
            else:
                results.append([current_start, currned_end])
                current_start = next_start
                currned_end = next_end
                

        results.append([current_start, currned_end])
        return results