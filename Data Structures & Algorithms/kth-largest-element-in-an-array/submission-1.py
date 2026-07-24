import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        # Solution 1
        # # sorting -> O(n log n)
        # nums.sort(reverse=True)
        # return nums[k-1]
       
        # Solution 2 - min heap 
        # # sorting -> O(n log k)
        # now it might confusing we choose min heap here when the question asks for findKthLargest

            # You are right that a Min-Heap keeps the smallest element at the top. 
            # we actually take advantage of that fact and because it keeps the smallest element at the top, 
            # everytime we want to insert a new element, we pop the smallest element at the root.

            #Idea:
            # inset first k elements from the input
            # heapify the k elements 
            # insert the rest of the elements one by one 
              # while inserting check if the incoming element is larger than current root. 
              # if it is, then pop the current root and then push 
            # finally return the root 

        heap = nums[:k] 
        heapq.heapify(heap)
        for num in nums[k:]:
            if num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, num)
        return heap[0]
