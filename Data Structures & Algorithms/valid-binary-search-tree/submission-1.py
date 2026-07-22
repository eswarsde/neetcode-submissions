# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # You are a node. Someone asks:
        # "What is the answer for the subtree rooted at you?"
        # Am I, and all the nodes beneath me, a valid Binary Search Tree?

        # 1) What do I need from parent / ancestors? - min_allowed, max_allowed => param
        # 

        # # 2) What do I need from children? True/False whether valid isValidBST # return val

        # # 3) At current node:
         # 

        if not root:
            return True
        

        def dfs(node, lower_bound, upper_bound):
            #Base Case
            if not node:
                return True

            # Problem-Specific Check & State Mutation
            if  node.val <= lower_bound or node.val >= upper_bound:
                return False


            # Prepare the value to be passed down - recurse & return
            return dfs(node.left, lower_bound, node.val) and dfs(node.right, node.val, upper_bound) 


        return  dfs(root, float('-inf'), float('inf'))
