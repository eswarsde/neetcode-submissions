class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)

        if n == k:
            return arr
        
        # sorting - O(n log n)
        # arr.sort(key= lambda num: (abs(num - x), num)) # for every element in the array calculates a tuple of 2 things 1) abs(num - x) and the num itself. and use this tuple to sort
        # return sorted(arr[:k])

        # approach 2:
        # because the list is already sorted, we can use binary search 
        # The primary purpose of the binary search algorithm is to quickly find the position of a specific target value within a sorted collection of data. 
        # if you see the output examples, they are always contigious. so we just need to understand the starting point 
        # that starting point has to be somewhere between 0 and n-k 

        left = 0
        right = n - k

        while left < right:
            mid = (left + right)//2
            # arr = [2,4,5,8], k = 2, x = 6, n=4
            # left = 0
            # right = 2
            # take a moment, the starting has to be 0, 1, 2
            # calculate mid = 0 + 2 //2 = 1 (// division returns quotient)
            # if we assume arr[mid] as the starting point i.e arr[1], the end point would be [mid+k-1] (1 + 2 -1) = 2
              # so essentially 1-2

              # now look at the question - An integer a is closer to x than an integer b if:  
              # "|a - x| < |b - x|" or "|a - x| == |b - x| and a < b", instead of "<=", we flip the condition to  >, which means b is closer to x

            # we are checking if the current starting point is closer to target/x or the element just outside of (1-2) is closer 
            # if the elment just outside is closer, then we slide the left pointer, our solution resides somewhere in the right
            if abs(arr[mid] - x) > abs(arr[mid+k] -x):
                left = mid+1
            else:
                right = mid
            
        return arr[left:left + k]







        


        

