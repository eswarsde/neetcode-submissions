# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        result = []
        queue = deque([root])

        while queue:
            num_nodes_in_level = len(queue)
            values_in_level = []

            for _ in range(num_nodes_in_level):
                node = queue.popleft()
                values_in_level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(values_in_level)




        return result

        