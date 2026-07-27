# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Return True if both binary trees are structurally identical with equal values.
    def isSameTree(self, p, q):
        # Recursive helper that compares one node from each tree.
        def dfs(node1, node2):
            # Base case: if both nodes are empty, this subtree matches.
            if node1 is None and node2 is None:
                # Two empty subtrees are the same.
                return True

            # If exactly one node is empty, the structures differ.
            if node1 is None or node2 is None:
                # One subtree has a node where the other does not.
                return False

            # If both nodes exist but values differ, trees are not the same here.
            if node1.val != node2.val:
                # Mismatched values mean mismatched trees.
                return False

            # Recurse into the left children to verify left subtrees match.
            left_same = dfs(node1.left, node2.left)

            # If left subtrees already differ, we can stop early.
            if left_same is False:
                # No need to check the right side once we know the answer is False.
                return False

            # Recurse into the right children to verify right subtrees match.
            right_same = dfs(node1.right, node2.right)

            # The current subtrees match only if both left and right match.
            return right_same

        # Start the DFS comparison from the two roots.
        return dfs(p, q)