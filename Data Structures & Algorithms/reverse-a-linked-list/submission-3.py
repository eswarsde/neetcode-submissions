# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # We walk through the list from left to right, and for each node, we redirect its next pointer to point to the node behind it.

        # Input: 0 -> 1 -> 2 -> 3 -> Null
        # Output: 3 -> 2 -> 1 -> 0 -> Null
        
        # curr Node - the current node we are processing
        # prev Node -> the node that should come after curr node once reversed
        # temp - the original next node

        # temp = curr.next
        # curr.next = prev
        # prev = curr
        # curr = temp

        prev, curr = None, head
        # curr = Node(0)
        # prev = None
        # we know we want Node(0).next = None
        # before we do that, let's save what is in Node(0).next in a temp = Node(1)
        # temp = curr.next
        # curr.next = prev
        # now we have linked Node(0) - None
        # we processed one Node correctly
        # for next iteration
        # make Node(0) as prev
        # make Node(1) as current
        # prev = curr
        # curr = temp
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

        