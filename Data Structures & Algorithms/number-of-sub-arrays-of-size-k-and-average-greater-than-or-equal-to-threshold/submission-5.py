class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # sum(arr[:k]) = k * t
        # sum of k elements in arr/k >= t
        # sum of k elements in arr = t * k
        n = len(arr)
        curr_sum = sum(arr[0:k])
        count = 0
        target = threshold * k

        if curr_sum >= target:
            count+=1
        
        for right in range(k,n):
            left = right - k 

            # remove
            curr_sum -= arr[left]

            # add
            curr_sum += arr[right]

            # see if the matches traget and increase
            if curr_sum >= target:
                count += 1




        return count






























































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