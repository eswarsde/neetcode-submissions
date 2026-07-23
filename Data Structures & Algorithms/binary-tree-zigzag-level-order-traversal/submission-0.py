# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        # Your code goes here
        if not root:
            return []

        result = []
        queue = deque([root])
        left_to_right = True # zig-zag flag

        while queue:
            num_nodes_at_level = len(queue)
            nodes_at_level = deque([])

            for _ in range(num_nodes_at_level):
                node = queue.popleft()

                if left_to_right:
                    nodes_at_level.append(node.val)
                else:
                    nodes_at_level.appendleft(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(list(nodes_at_level))
            left_to_right = not left_to_right #Flip the toggle for the next level

        return result

