# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findLeaves(self, root):
        # This will store values grouped by removal round / bottom-up height.
        ans = []

        def dfs(node):
            # Base case / visited-empty-child case:
            # return -1 so a real leaf becomes 0 via 1 + max(-1, -1).
            if node is None:
                return -1

            # Enter this node's state:
            # first solve both children because this is postorder DFS.
            left_height = dfs(node.left)
            right_height = dfs(node.right)

            # Current work:
            # derive this node's removal round from its deepest child.
            height = 1 + max(left_height, right_height)

            # If this is the first node we have seen for this round,
            # create a new bucket for that round.
            if height == len(ans):
                ans.append([])

            # Place this node into the group for its removal round.
            ans[height].append(node.val)

            # Return value:
            # give the parent this node's computed bottom-up height.
            return height

        # Start traversal from the root. The DFS fills ans as a side effect.
        dfs(root)

        return ans