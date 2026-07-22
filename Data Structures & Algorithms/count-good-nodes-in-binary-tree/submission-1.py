# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        count = 0
        def dfs(node, maxseen_so_far):
            nonlocal count
            # base condition
            # # What does an empty node contribute to the answer?
            if not node:
                return
            # Problem-Specific Check & State Mutation

            if node.val >= maxseen_so_far:
                count+=1

            #  4. Prepare the value to be passed down
            new_max = max(maxseen_so_far, node.val)
            # recurse
            dfs(node.left, new_max)
            dfs(node.right, new_max)


        dfs(root, root.val)
        return count
        

        