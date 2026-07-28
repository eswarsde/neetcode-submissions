# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        best_length = 0
        def dfs(node):
            nonlocal best_length
            if node is None:
                return 0

            left_height = dfs(node.left)
            right_height = dfs(node.right)

            # Complete path through this node.
            # Diameter is measured in edges.
            best_length = max(best_length, left_height + right_height)


            # Extendable one-sided path returned to parent.
            # +1 includes the current node.
            return 1 + max(left_height, right_height)

        dfs(root)

        return best_length


        