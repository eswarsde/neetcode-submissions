# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None or head.next is None:
            return head

    #     # 0 -> 1 -> 2 -> 3 -> None
        
    #     # 3 -> 2 ->1 ->0 -> None
  
    #    # initial state
    #     current = 0
    #     prev = None
    #    # what we have access to when on current ListNode
    #     next_node = current.next (1)
    #     # what we want 1) Save the next_node(1) and Flip (0 -> 1 => 0-> None) 
    #     current.next = prev 
    #
    #
    #     next_node = current (1.next = )
    #    

        prev = None
        current = head

        while current is not None:
            next_node = current.next # what we have access in current ListNode
            current.next = prev 
            
            prev = current
            current = next_node
        
        return prev 