import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        # # solution 1
        # # sorting -> O(n log n)
        # nums.sort(reverse=True)
        # return nums[k-1]

        # # solution 2 - min heap 
        # # sorting -> O(n log k)

        heap = nums[:k] 
        heapq.heapify(heap)
        for num in nums[k:]:
            if num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, num)
        
        return heap[0]
