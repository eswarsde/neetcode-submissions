class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        result = 0
        window_sum = 0
        n = len(arr)


        for right in range(n):
            window_sum += arr[right]

            if right >= k:
                window_sum -= arr[right -k]
            
            if right >= k-1:
                
                if window_sum/k >= threshold:
                    result+=1

        return result