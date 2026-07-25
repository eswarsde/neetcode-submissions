# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # each list is sorted in ascending order.

        # Idea keep head of each List in a min heap, o(1) to get the list with smallest head

        if not lists:
            return None

        counter = 0
        min_heap = []
        for node in lists:
            if node:  # skip empty lists
                heapq.heappush(min_heap, (node.val, counter, node))
                counter += 1

        result = ListNode()
        curr_node = result

        while min_heap:
            _, _, node = heapq.heappop(min_heap)
            curr_node.next = node
            curr_node = node

            if node.next:
                heapq.heappush(min_heap, (node.next.val, counter, node.next))
                counter+=1




        return result.next
                