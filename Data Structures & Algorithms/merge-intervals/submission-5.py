class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals
            
        intervals.sort()
        result = [intervals[0]]

        for current_start, current_end in intervals[1:]:
            prev_start, prev_end = result[-1] 
            if current_start <= prev_end:
                prev_end = max(prev_end, current_end)
                result[-1][1] = prev_end
            else:
                result.append([current_start, current_end]) 

        return result

      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      


      
      
      
      
      
      
      
        if len(intervals) <=1:
            return intervals

        intervals.sort()
        results = []

        current_start = intervals[0][0]
        current_end = intervals[0][1]

        for i in range(1, len(intervals)):
            next_start = intervals[i][0]
            next_end = intervals[i][1]

            if next_start <= current_end:
                currned_end = max(current_end, next_end)
            else:
                results.append([current_start, current_end])
                current_start = next_start
                currned_end = next_end
                

        results.append([current_start, current_end])
        return results