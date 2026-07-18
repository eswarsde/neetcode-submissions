# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None or head.next is None:
            return head

    #     # 0 -> 1 -> 2 -> 3
        
    #     # 3->2->1->0
  
    #    # initial state
    #     prev = None
    #     current = 0
    #     next_node =  (1)
        
    #     # what we want
    #     current.next = prev
    #     next_node.next = current
    #    

        prev = None
        current = head

        while current is not None:

            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        return prev 