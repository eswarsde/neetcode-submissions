# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head, val):
        # Dummy node lets us remove the original head using the same logic
        # as any other node, so we avoid a special-case branch.
        dummy = ListNode(0, head)

        # current always points to the node BEFORE the node we may remove.
        current = dummy

        # Stop when there is no next node left to inspect.
        while current.next is not None:
            # Current work:
            # inspect the next node and decide whether to delete it or keep it.
            if current.next.val == val:
                # Remove the next node by skipping over it.
                # We do NOT move current here, because the new current.next
                # might also need to be removed.
                current.next = current.next.next
            else:
                # Keep this next node, so advance current forward.
                current = current.next

        # Return the real head, which may have changed if original head nodes
        # were removed.
        return dummy.next
        