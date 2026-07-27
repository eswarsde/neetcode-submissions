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

            best_length = max(best_length, left_height + right_height)
            return 1 + max(left_height, right_height)

        dfs(root)

        return best_length


        