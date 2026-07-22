# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []


        result = []        
        queue = deque([root])

        while queue:
            num_nodes_at_level = len(queue)

            for i in range(num_nodes_at_level):

                node = queue.popleft()

                # Because we queued Right then Left, the 0th index is ALWAYS our rightmost node!
                if i == 0:
                    result.append(node.val)

                # Queue right child FIRST
                if node.right:
                    queue.append(node.right)
                # Queue left child SECOND
                if node.left:
                    queue.append(node.left)

        return result


        
        